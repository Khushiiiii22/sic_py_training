# app/__init__.py
from flask import Flask
import os

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_pyfile(
        os.path.join(os.path.dirname(__file__), '../config.py')
    )
    # Ensure static folders exist
    os.makedirs(os.path.join(app.static_folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(app.static_folder, 'css'), exist_ok=True)
    os.makedirs(os.path.join(app.static_folder, 'js'), exist_ok=True)

    from . import routes
    app.register_blueprint(routes.bp)
    return app
