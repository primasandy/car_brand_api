# app/models.py

from app import db

class Price(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('car_brands.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "currency": self.currency,
            "brand_id": self.brand_id
        }

class Production(db.Model):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('car_brands.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "year": self.year,
            "brand_id": self.brand_id
        }

class CarBrand(db.Model):
    __tablename__ = 'car_brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relasi ke tabel harga dan produksi
    prices = db.relationship('Price', backref='car_brand', lazy=True)
    productions = db.relationship('Production', backref='car_brand', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
