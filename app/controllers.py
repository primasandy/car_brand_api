# app/controllers.py

from app.models import CarBrand, Price, Production
from app import db

def get_prices():
    return [price.to_dict() for price in Price.query.all()]

# Fungsi untuk CarBrand
def get_all_car_brands():
    return [car_brand.to_dict() for car_brand in CarBrand.query.all()]

def add_car_brand(name):
    new_car_brand = CarBrand(name=name)
    db.session.add(new_car_brand)
    db.session.commit()
    return new_car_brand.to_dict()

def update_car_brand(brand_id, name):
    car_brand = CarBrand.query.get(brand_id)
    if car_brand:
        car_brand.name = name
        db.session.commit()
        return car_brand.to_dict()
    return None

def delete_car_brand(brand_id):
    car_brand = CarBrand.query.get(brand_id)
    if car_brand:
        db.session.delete(car_brand)
        db.session.commit()
        return True
    return False

# Fungsi untuk Price
def add_price(amount, currency, brand_id):
    new_price = Price(amount=amount, currency=currency, brand_id=brand_id)
    db.session.add(new_price)
    db.session.commit()
    return new_price.to_dict()

def update_price(price_id, amount, currency):
    price = Price.query.get(price_id)
    if price:
        price.amount = amount
        price.currency = currency
        db.session.commit()
        return price.to_dict()
    return None

def delete_price(price_id):
    price = Price.query.get(price_id)
    if price:
        db.session.delete(price)
        db.session.commit()
        return True
    return False

def get_productions():
    return [production.to_dict() for production in Production.query.all()]

# Fungsi untuk Production
def add_production(location, year, brand_id):
    new_production = Production(location=location, year=year, brand_id=brand_id)
    db.session.add(new_production)
    db.session.commit()
    return new_production.to_dict()

def update_production(production_id, location, year):
    production = Production.query.get(production_id)
    if production:
        production.location = location
        production.year = year
        db.session.commit()
        return production.to_dict()
    return None

def delete_production(production_id):
    production = Production.query.get(production_id)
    if production:
        db.session.delete(production)
        db.session.commit()
        return True
    return False
