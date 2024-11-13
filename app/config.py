import os

class Config:
    # URL database, bisa disesuaikan untuk MySQL atau SQLite
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/car_brands_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
