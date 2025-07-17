import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from textblob import TextBlob
from config import DATA_DIR
import time

# Ensure matplotlib is backend-agnostic for servers
import matplotlib
matplotlib.use('Agg')

# ------------- Plot Style -------------
plt.style.use('ggplot')
sns.set_palette("pastel")
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

# ------------- Data Paths -------------
DEFAULT_PRODUCT_CSV = os.path.join(DATA_DIR, 'nykaa.csv')
DEFAULT_REVIEW_CSV = os.path.join(DATA_DIR, 'nykaa_review.csv')
DEFAULT_BRANDS_CSV = os.path.join(DATA_DIR, 'nyka_popular_brands_products_2022_10_16.csv')

def load_data(filepaths=None):
    try:
        if filepaths:
            products_path = filepaths.get('products', DEFAULT_PRODUCT_CSV)
            reviews_path = filepaths.get('reviews', DEFAULT_REVIEW_CSV)
            brands_path  = filepaths.get('brands',  DEFAULT_BRANDS_CSV)
        else:
            products_path, reviews_path, brands_path = DEFAULT_PRODUCT_CSV, DEFAULT_REVIEW_CSV, DEFAULT_BRANDS_CSV

        products_df = pd.read_csv(products_path)
        reviews_df  = pd.read_csv(reviews_path)
        brands_df   = pd.read_csv(brands_path)
        return products_df, reviews_df, brands_df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return (
            pd.DataFrame(columns=['name', 'brand', 'price', 'rating', 'rating_count', 'category']),
            pd.DataFrame(columns=['product_id', 'rating', 'review']),
            pd.DataFrame(columns=['brand', 'product_name', 'price', 'rating'])
        )

def clean_data(products_df, reviews_df, brands_df):
    """ Data cleaning pipeline for your custom Nykaa files. """
    try:
        # ------ RENAME COLUMNS TO STANDARD NAMES ------
        products_df = products_df.rename(columns={
            'Product Brand': 'brand',
            'Product Rating': 'rating',
            'Product Price': 'price',
            'Product Name': 'name',
            'Product Category': 'category',
            'Product Reviews Count': 'rating_count'
        })

        reviews_df = reviews_df.rename(columns={
            'content': 'review'
        })

        brands_df = brands_df.rename(columns={
            'brand_name': 'brand',
            'price': 'price',
            'rating': 'rating',
            'rating_count': 'rating_count',
            'product_title': 'product_name'
        })

        products_df.columns = products_df.columns.str.lower()
        reviews_df.columns  = reviews_df.columns.str.lower()
        brands_df.columns   = brands_df.columns.str.lower()

        # --------- Default/Fill Missing Key Columns ---------
        if 'rating_count' not in products_df.columns: products_df['rating_count'] = 0
        if 'rating' not in products_df.columns:       products_df['rating']       = 0
        if 'price' not in products_df.columns:        products_df['price']        = '₹0'
        if 'category' not in products_df.columns:     products_df['category']     = 'Uncategorized'
        products_df = products_df.fillna({
            'rating': 0,
            'rating_count': 0,
            'price': '₹0',
            'category': 'Uncategorized'
        })

        if 'review' not in reviews_df.columns: reviews_df['review'] = 'No review text'
        reviews_df = reviews_df.fillna({'review': 'No review text'})
        if 'price' not in brands_df.columns: brands_df['price'] = '₹0'

        # -------- Clean price fields robustly --------
        for df in [products_df, brands_df]:
            if 'price' in df.columns:
                df['price'] = (
                    df['price']
                    .astype(str)
                    .str.extract(r'([\d,.]+)', expand=False)
                    .str.replace(',', '', regex=False)
                )
                df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)

        # -------- Clip/clean ratings if present --------
        if 'rating' in products_df.columns:
            products_df['rating'] = pd.to_numeric(products_df['rating'], errors='coerce').clip(0, 5).fillna(0)
        if 'rating' in reviews_df.columns:
            reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce').clip(0, 5).fillna(0)
        if 'rating' in brands_df.columns:
            brands_df['rating'] = pd.to_numeric(brands_df['rating'], errors='coerce').clip(0, 5).fillna(0)

        # -------- Main category extraction --------
        if 'category' in products_df.columns:
            products_df['main_category'] = (
                products_df['category']
                .astype(str)
                .str.split('|')
                .str[0]
                .str.strip()
                .fillna('Uncategorized')
            )
        return products_df, reviews_df, brands_df
    except Exception as e:
        print(f"Error cleaning data: {str(e)}")
        return products_df, reviews_df, brands_df


def save_plot(fig, filename, dpi=100):
    """Save a matplotlib figure."""
    try:
        images_path = os.path.join('static', 'images')
        os.makedirs(images_path, exist_ok=True)
        path = os.path.join(images_path, filename)
        fig.savefig(path, bbox_inches='tight', dpi=dpi, facecolor=fig.get_facecolor())
        print(f"Saved plot to: {path}")  # Debug print: lets you trace output!
        plt.close(fig)
        return path
    except Exception as e:
        print(f"Error saving plot: {str(e)}")
        return None

def generate_summary_stats(products_df, reviews_df):
    """Calculate dashboard key statistics and quick leaderboard."""
    stats = {}
    stats['total_products'] = len(products_df)
    stats['total_brands'] = products_df['brand'].nunique() if not products_df.empty else 0
    stats['avg_rating'] = products_df['rating'].mean() if not products_df.empty else 0
    stats['avg_price'] = products_df['price'].mean() if not products_df.empty else 0
    stats['total_reviews'] = len(reviews_df)
    if not products_df.empty and products_df['brand'].nunique() > 0:
        stats['top_brand'] = products_df['brand'].value_counts().idxmax()
    else:
        stats['top_brand'] = "N/A"
    if not products_df.empty and (products_df['rating'] > 0).any():
        stats['top_rated_product'] = products_df.loc[products_df['rating'].idxmax()]['name']
    else:
        stats['top_rated_product'] = "N/A"
    # For the leaderboard of top products (>=100 reviews)
    if 'rating_count' in products_df.columns and not products_df.empty:
        filtered = products_df[products_df['rating_count'] >= 100].copy()
        top_products = filtered.sort_values(['rating', 'rating_count'], ascending=[False, False]).head(10)
        stats['top_products'] = top_products
    else:
        stats['top_products'] = pd.DataFrame()
    return {k: round(v, 2) if isinstance(v, float) else v for k, v in stats.items()}

def analyze_ratings(reviews_df):
    """
    Plot rating distribution (pie/bar) and monthly trend (if available).
    - Always generates bar.
    - Pie is generated if there are <=7 distinct ratings AND all are nonzero.
    """
    results = {}
    if reviews_df.empty or 'rating' not in reviews_df.columns:
        print("[DEBUG] No ratings data to plot.")  # Helps with debugging!
        return results

    rating_counts = reviews_df['rating'].value_counts().sort_index()
    print(f"[DEBUG] Ratings found: {dict(rating_counts)}")  # Debugging print
    num_grps = len(rating_counts)
    
    # Pie chart if suitable (few categories and all nonzero)
    if 2 <= num_grps <= 7 and not (rating_counts == 0).any():
        fig1, ax1 = plt.subplots(figsize=(10, 8))
        ax1.pie(
            rating_counts,
            labels=rating_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 0.5}
        )
        ax1.set_title('Rating Distribution', pad=20)
        results['rating_pie'] = save_plot(fig1, 'rating_pie.png')

    # Bar chart (always)
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=rating_counts.index,
        y=rating_counts.values,
        ax=ax2,
        palette='Blues_r'
    )
    ax2.set_title('Rating Distribution')
    ax2.set_xlabel('Rating')
    ax2.set_ylabel('Count')
    for p in ax2.patches:
        ax2.annotate(
            f'{p.get_height():.0f}',
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center',
            xytext=(0, 5),
            textcoords='offset points'
        )
    results['rating_bar'] = save_plot(fig2, 'rating_bar.png')

    # Monthly trend
    if 'review_date' in reviews_df.columns:
        if not pd.api.types.is_datetime64_any_dtype(reviews_df['review_date']):
            reviews_df['review_date'] = pd.to_datetime(reviews_df['review_date'], errors='coerce')
        reviews_df['month'] = reviews_df['review_date'].dt.to_period('M')
        monthly_ratings = reviews_df.groupby('month')['rating'].mean()
        if not monthly_ratings.empty:
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            monthly_ratings.plot(ax=ax3, marker='o', color='#d62e71')
            ax3.set_title('Average Rating Over Time', pad=20)
            ax3.set_xlabel('Month')
            ax3.set_ylabel('Average Rating')
            ax3.grid(True, alpha=0.3)
            results['rating_trend'] = save_plot(fig3, 'rating_trend.png')
    return results

def analyze_brands(products_df):
    """Analyze brands: top counts (bar+pie), price distribution (box)."""
    results = {}
    if products_df.empty or 'brand' not in products_df.columns:
        return results
    top_brands = products_df['brand'].value_counts().head(10)
    if top_brands.empty:
        return results

    # Bar chart (always)
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=top_brands.values,
        y=top_brands.index,
        ax=ax1,
        palette='viridis_r'
    )
    ax1.set_title('Top 10 Brands by Product Count', pad=20)
    ax1.set_xlabel('Number of Products')
    ax1.set_ylabel('Brand')
    for i, v in enumerate(top_brands.values):
        ax1.text(v + 2, i, str(v), color='black', va='center')
    results['brand_count'] = save_plot(fig1, 'brand_count.png')
    results['brand_counts'] = top_brands

    # Pie chart if few brands
    if 2 <= len(top_brands) <= 7 and not (top_brands == 0).any():
        figpie, axpie = plt.subplots(figsize=(8, 8))
        axpie.pie(
            top_brands.values,
            labels=top_brands.index,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 0.5}
        )
        axpie.set_title('Top Brands Share')
        results['brand_pie'] = save_plot(figpie, 'brand_pie.png')

    # Boxplot for price distribution among top brands
    top_brand_list = top_brands.index.tolist()
    price_df = products_df[products_df['brand'].isin(top_brand_list)]
    if not price_df.empty:
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        sns.boxplot(
            x='brand',
            y='price',
            data=price_df,
            ax=ax2,
            palette='Set3'
        )
        ax2.set_title('Price Distribution by Brand', pad=20)
        ax2.set_xlabel('Brand')
        ax2.set_ylabel('Price (₹)')
        ax2.tick_params(axis='x', rotation=45)
        results['brand_price'] = save_plot(fig2, 'brand_price.png')
    return results

def analyze_pricing(products_df):
    """Price analysis: histogram, price-range pie, scatter price-rating."""
    results = {}
    if products_df.empty or 'price' not in products_df.columns or 'rating' not in products_df.columns:
        return results
    # Histogram
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.histplot(
        products_df['price'],
        bins=30,
        kde=True,
        ax=ax1,
        color='skyblue'
    )
    ax1.set_title('Product Price Distribution', pad=20)
    ax1.set_xlabel('Price (₹)')
    ax1.set_ylabel('Count')
    if not products_df['price'].empty:
        ax1.set_xlim(0, products_df['price'].quantile(0.95))
    results['price_dist'] = save_plot(fig1, 'price_dist.png')

    # Price-range pie
    price_bins = pd.cut(products_df['price'], bins=7)
    price_bin_counts = price_bins.value_counts().sort_index()
    if 2 <= price_bin_counts.shape[0] <= 7:
        figpie, axpie = plt.subplots(figsize=(8, 8))
        axpie.pie(
            price_bin_counts,
            labels=[str(i) for i in price_bin_counts.index],
            autopct='%1.1f%%',
            startangle=90
        )
        axpie.set_title('Price Ranges Share')
        results['price_pie'] = save_plot(figpie, 'price_pie.png')

    # Scatter plot: price vs. rating
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.scatterplot(
        x='price',
        y='rating',
        data=products_df,
        ax=ax2,
        alpha=0.6,
        hue='rating',
        palette='coolwarm'
    )
    ax2.set_title('Price vs. Rating', pad=20)
    ax2.set_xlabel('Price (₹)')
    ax2.set_ylabel('Rating')
    if not products_df['price'].empty:
        ax2.set_xlim(0, products_df['price'].quantile(0.95))
    results['price_rating'] = save_plot(fig2, 'price_rating.png')

    # Table: avg price by brand
    if 'brand' in products_df.columns:
        avg_by_brand = products_df.groupby('brand')['price'].mean().sort_values(ascending=False).head(10)
        results['avg_price_by_brand'] = avg_by_brand
    return results

def analyze_categories(products_df):
    """Category analysis (count, pie chart, avg price)."""
    results = {}
    if products_df.empty or 'main_category' not in products_df.columns:
        return results
    top_cats = products_df['main_category'].value_counts().head(10)

    # Bar plot (always)
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=top_cats.values,
        y=top_cats.index,
        ax=ax1,
        palette='magma_r'
    )
    ax1.set_title('Top 10 Product Categories', pad=20)
    ax1.set_xlabel('Number of Products')
    ax1.set_ylabel('Category')
    for i, v in enumerate(top_cats.values):
        ax1.text(v + 2, i, str(v), color='black', va='center')
    results['category_count'] = save_plot(fig1, 'category_count.png')
    results['top_categories'] = top_cats

    # Pie chart if few categories
    if 2 <= len(top_cats) <= 7 and not (top_cats == 0).any():
        figpie, axpie = plt.subplots(figsize=(8, 8))
        axpie.pie(
            top_cats.values,
            labels=top_cats.index,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 0.5}
        )
        axpie.set_title('Top Categories Share')
        results['category_pie'] = save_plot(figpie, 'category_pie.png')

    # Avg price by category bar (always)
    cat_prices = products_df.groupby('main_category')['price'].mean().sort_values(ascending=False).head(10)
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=cat_prices.values,
        y=cat_prices.index,
        ax=ax2,
        palette='flare_r'
    )
    ax2.set_title('Average Price by Category', pad=20)
    ax2.set_xlabel('Average Price (₹)')
    ax2.set_ylabel('Category')
    for i, v in enumerate(cat_prices.values):
        ax2.text(v + 20, i, f'₹{v:.2f}', color='black', va='center')
    results['category_price'] = save_plot(fig2, 'category_price.png')
    return results

def analyze_sentiment(reviews_df):
    """Sentiment analysis: histogram, categorical bar/pie if small group count."""
    results = {}
    if 'review' not in reviews_df.columns or reviews_df.empty:
        return results
    # Use a random sample if large
    sample_reviews = reviews_df['review'].dropna()
    if len(sample_reviews) > 1000:
        sample_reviews = sample_reviews.sample(1000, random_state=42)

    # Sentiment scores
    sentiments = sample_reviews.apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    # Histogram
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.histplot(sentiments, bins=20, kde=True, ax=ax1, color='purple')
    ax1.set_title('Review Sentiment Distribution', pad=20)
    ax1.set_xlabel('Sentiment Polarity')
    ax1.set_ylabel('Count')
    ax1.axvline(0, color='red', linestyle='--')
    results['sentiment_dist'] = save_plot(fig1, 'sentiment_dist.png')

    # Buckets for sentiment categories (bar)
    sentiment_labels = pd.cut(
        sentiments,
        bins=[-1, -0.5, -0.1, 0.1, 0.5, 1],
        labels=['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']
    )
    sentiment_bucket_counts = sentiment_labels.value_counts().sort_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.countplot(
        x=sentiment_labels,
        ax=ax2,
        order=['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive'],
        palette='RdYlGn'
    )
    ax2.set_title('Sentiment Categories', pad=20)
    ax2.set_xlabel('Sentiment')
    ax2.set_ylabel('Count')
    for p in ax2.patches:
        ax2.annotate(
            f'{p.get_height():.0f}',
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center',
            xytext=(0, 5),
            textcoords='offset points'
        )
    results['sentiment_cats'] = save_plot(fig2, 'sentiment_cats.png')

    # Pie for buckets if few groups
    valid_buckets = sentiment_bucket_counts[sentiment_bucket_counts > 0]
    if 2 <= len(valid_buckets) <= 5:
        figpie, axpie = plt.subplots(figsize=(7, 7))
        axpie.pie(
            valid_buckets,
            labels=valid_buckets.index,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 0.5}
        )
        axpie.set_title('Sentiment Share')
        results['sentiment_pie'] = save_plot(figpie, 'sentiment_pie.png')

    return results

def perform_full_analysis(filepaths=None):
    """
    Main entry: run full analysis and return result dict.
    :param filepaths: Optional dict {'products', 'reviews', 'brands'}
    :returns: dict with all results and plot paths
    """
    import time
    start_time = time.time()
    print("Starting comprehensive analysis...")
    results = {
        'summary': {},
        'ratings': {},
        'brands': {},
        'pricing': {},
        'categories': {},
        'sentiment': {},
        'execution_time': None
    }
    try:
        products_df, reviews_df, brands_df = load_data(filepaths)
        products_df, reviews_df, brands_df = clean_data(products_df, reviews_df, brands_df)

        # Each section safely
        try:
            results['summary'] = generate_summary_stats(products_df, reviews_df)
        except Exception as e:
            print(f"[WARN] Error in summary stats: {e}")

        try:
            results['ratings'] = analyze_ratings(reviews_df)
        except Exception as e:
            print(f"[WARN] Error in ratings analysis: {e}")

        try:
            results['brands'] = analyze_brands(products_df)
        except Exception as e:
            print(f"[WARN] Error in brands analysis: {e}")

        try:
            results['pricing'] = analyze_pricing(products_df)
        except Exception as e:
            print(f"[WARN] Error in pricing analysis: {e}")

        try:
            results['categories'] = analyze_categories(products_df)
        except Exception as e:
            print(f"[WARN] Error in categories analysis: {e}")

        try:
            results['sentiment'] = analyze_sentiment(reviews_df)
        except Exception as e:
            print(f"[WARN] Error in sentiment analysis: {e}")

        results['execution_time'] = round(time.time() - start_time, 2)
        print(f"Analysis completed in {results['execution_time']} seconds")
        return results
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        results['error'] = str(e)
        results['execution_time'] = round(time.time() - start_time, 2)
        return results


