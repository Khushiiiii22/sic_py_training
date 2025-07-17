import os

# Absolute path to the folder this config.py is in (usually your app root)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Path to your data folder where the CSVs live
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Flask secret key -- change to a random string before deploying!
SECRET_KEY = 'your-secret-key-here'

# Optional: use for debugging or testing settings if needed
DEBUG = False
TESTING = False

# Example for future: if you want a separate folder for uploads, you can add:
# UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

# Example usage in your analysis.py or anywhere else:
# DEFAULT_PRODUCT_CSV = os.path.join(DATA_DIR, 'nykaa.csv')
# DEFAULT_REVIEW_CSV = os.path.join(DATA_DIR, 'nykaa_review.csv')
# DEFAULT_BRANDS_CSV = os.path.join(DATA_DIR, 'nyka_popular_brands_products_2022_10_16.csv')

