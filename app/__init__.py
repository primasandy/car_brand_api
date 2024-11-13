# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Inisialisasi database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi database dengan aplikasi
    db.init_app(app)

    # Import models dan views setelah inisialisasi db
    with app.app_context():
        from app import models, views
        db.create_all()  # Membuat tabel jika belum ada

        # Daftarkan Blueprint
        app.register_blueprint(views.car_brand_bp)

    return app
