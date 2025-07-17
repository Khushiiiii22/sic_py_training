from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from .analysis import perform_full_analysis, load_data, clean_data, generate_summary_stats
import os
import uuid
from pathlib import Path
import pandas as pd
import traceback

bp = Blueprint('main', __name__)

# Configure upload and image directories
UPLOAD_DIR = Path(__file__).parent / "data" / "uploads"
IMAGE_DIR = Path(__file__).parent / "static" / "images"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

def get_image_url(plot_path):
    """
    Converts a static plot's path into a URL for use in templates.
    Returns None if the plot_path is falsy.
    Accepts either a direct file path or a dict with filename.
    """
    if not plot_path:
        return None
    if isinstance(plot_path, dict):
        return url_for('static', filename=f'images/{plot_path.get("filename")}')
    if isinstance(plot_path, str):
        if plot_path.startswith('/static/') or plot_path.startswith('http'):
            return plot_path
        filename = Path(plot_path).name
        return url_for('static', filename=f'images/{filename}')
    return None

@bp.route('/')
def index():
    """Homepage with dashboard summary stats."""
    try:
        products_df, reviews_df, brands_df = load_data()
        products_df, reviews_df, brands_df = clean_data(products_df, reviews_df, brands_df)
        summary = generate_summary_stats(products_df, reviews_df)
        return render_template('index.html', summary=summary)
    except Exception as e:
        traceback.print_exc()
        flash(f"Error loading data: {str(e)}", "danger")
        return render_template('index.html', summary={
            'total_products': 0,
            'total_brands': 0,
            'avg_rating': 0,
            'avg_price': 0,
            'total_reviews': 0,
            'top_brand': "N/A",
            'top_rated_product': "N/A"
        })

@bp.route('/ratings')
def ratings():
    try:
        results = perform_full_analysis()
        return render_template('ratings.html',
            rating_pie=get_image_url(results.get('ratings', {}).get('rating_pie')),
            rating_bar=get_image_url(results.get('ratings', {}).get('rating_bar')),
            rating_trend=get_image_url(results.get('ratings', {}).get('rating_trend')),
            summary=results.get('summary', {})
        )
    except Exception as e:
        traceback.print_exc()
        flash(f"Error generating ratings analysis: {str(e)}", "danger")
        return redirect(url_for('main.index'))

@bp.route('/brands')
def brands():
    try:
        results = perform_full_analysis()
        brands_section = results.get('brands', {})
        brand_counts = brands_section.get('brand_counts', {})
        # Fix: convert Series (or DataFrame) to dict
        if hasattr(brand_counts, "to_dict"):
            brand_counts = brand_counts.to_dict()
        return render_template('brands.html',
            brand_count=get_image_url(brands_section.get('brand_count')),
            brand_pie=get_image_url(brands_section.get('brand_pie')),
            brand_price=get_image_url(brands_section.get('brand_price')),
            brand_counts=brand_counts,
            summary=results.get('summary', {})
        )
    except Exception as e:
        traceback.print_exc()
        flash(f"Error generating brand analysis: {str(e)}", "danger")
        return redirect(url_for('main.index'))

@bp.route('/pricing')
def pricing():
    try:
        results = perform_full_analysis()
        pricing_section = results.get('pricing', {})
        avg_price_by_brand = pricing_section.get('avg_price_by_brand', {})
        # Fix: convert Series or DataFrame to dict if needed
        if hasattr(avg_price_by_brand, "to_dict"):
            avg_price_by_brand = avg_price_by_brand.to_dict()
        return render_template('pricing.html',
            price_dist=get_image_url(pricing_section.get('price_dist')),
            price_pie=get_image_url(pricing_section.get('price_pie')),
            price_rating=get_image_url(pricing_section.get('price_rating')),
            avg_price=results.get('summary', {}).get('avg_price', 0),
            avg_price_by_brand=avg_price_by_brand,
            summary=results.get('summary', {})
        )
    except Exception as e:
        traceback.print_exc()
        flash(f"Error generating pricing analysis: {str(e)}", "danger")
        return redirect(url_for('main.index'))

@bp.route('/products')
def products():
    try:
        results = perform_full_analysis()
        summary = results.get('summary', {})
        top_products = summary.get('top_products', pd.DataFrame())
        # Fix: always convert to list-of-dicts for Jinja
        if isinstance(top_products, pd.DataFrame):
            top_products = top_products.to_dict('records')
        return render_template('products.html',
            top_products=top_products,
            top_brand=summary.get('top_brand', "N/A"),
            top_rated_product=summary.get('top_rated_product', "N/A"),
            summary=summary
        )
    except Exception as e:
        traceback.print_exc()
        flash(f"Error generating products analysis: {str(e)}", "danger")
        return redirect(url_for('main.index'))

@bp.route('/upload-csv', methods=['GET', 'POST'])
def upload_csv():
    """
    CSV upload endpoint:
      - On POST, save files, analyze, and render results.
      - On GET, shows upload form.
    """
    if request.method == 'POST':
        try:
            filepaths = {}
            for key in ['products', 'reviews', 'brands']:
                uploaded_file = request.files.get(key)
                if uploaded_file and uploaded_file.filename:
                    filename = f"{uuid.uuid4()}_{uploaded_file.filename}"
                    path = UPLOAD_DIR / filename
                    uploaded_file.save(path)
                    filepaths[key] = str(path)

            # Run analysis on uploaded files
            results = perform_full_analysis(filepaths)

            # Convert chart filepaths to URLs for web display
            for section in results:
                if isinstance(results[section], dict):
                    for k, v in results[section].items():
                        if isinstance(v, str) and (
                            k.endswith('_pie') or k.endswith('_bar') or k.endswith('_count') or
                            k.endswith('_price') or k.endswith('_dist') or k.endswith('_trend') or k.endswith('_cats')
                        ):
                            results[section][k] = get_image_url(v)

            # Ensure top_products is always a list of dicts for template
            if 'summary' in results and 'top_products' in results['summary']:
                top_products = results['summary']['top_products']
                if isinstance(top_products, pd.DataFrame):
                    results['summary']['top_products'] = top_products.to_dict('records')

            return render_template('analysis_results.html', results=results)

        except Exception as e:
            traceback.print_exc()
            flash(f"Error analyzing uploaded files: {str(e)}", "danger")
            return redirect(url_for('main.upload_csv'))
    return render_template('upload_csv.html')

@bp.route('/static/images/<filename>')
def serve_image(filename):
    """Serve image files for plots if needed explicitly."""
    return send_from_directory(IMAGE_DIR, filename)

@bp.route('/refresh-data')
def refresh_data():
    """
    If perform_full_analysis uses functools.lru_cache or similar,
    this will clear the cache for a hard data refresh.
    """
    if hasattr(perform_full_analysis, 'cache_clear'):
        perform_full_analysis.cache_clear()
        flash("Data cache cleared. Next dashboard load will re-analyze fresh data.", "success")
    else:
        flash("No cache is in use, so nothing to refresh.", "warning")
    return redirect(url_for('main.index'))
