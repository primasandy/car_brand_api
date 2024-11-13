from flask import jsonify, request, Blueprint
from app.controllers import (
    get_all_car_brands, add_car_brand, update_car_brand, delete_car_brand,
    add_price, get_prices, update_price, delete_price,
    add_production, get_productions, update_production, delete_production
)

# Inisialisasi Blueprint untuk memisahkan views
car_brand_bp = Blueprint('car_brand_bp', __name__)

# Route untuk halaman utama dengan informasi endpoint
@car_brand_bp.route('/', methods=['GET'])
def index():
    info = {
        "message": "Welcome to the Car Brand API!",
        "endpoints": {
            "GET /api/car-brands": "Retrieve a list of car brands.",
            "POST /api/car-brand": "Add a new car brand. Use JSON body with format {'name': 'Toyota'}",
            "PUT /api/car-brand/<id>": "Update car brand by ID. Use JSON body {'name': 'Toyota'}",
            "DELETE /api/car-brand/<id>": "Delete car brand by ID",
            "GET /api/prices": "Retrieve a list of car prices.",
            "POST /api/price": "Add a new price. Use JSON body with format {'amount': 30000, 'currency': 'USD', 'brand_id': 1}",
            "PUT /api/price/<id>": "Update price by ID. Use JSON body {'amount': 35000, 'currency': 'USD'}",
            "DELETE /api/price/<id>": "Delete price by ID",
            "GET /api/productions": "Retrieve a list of car production locations.",
            "POST /api/production": "Add a new production location. Use JSON body {'location': 'Japan', 'year': 2022, 'brand_id': 1}",
            "PUT /api/production/<id>": "Update production by ID. Use JSON body {'location': 'Japan', 'year': 2023}",
            "DELETE /api/production/<id>": "Delete production by ID"
        }
    }
    return jsonify(info), 200

# Endpoint untuk CarBrand
@car_brand_bp.route('/api/car-brands', methods=['GET'])
def get_car_brands():
    car_brands = get_all_car_brands()
    return jsonify({
        "status": "success",
        "data": car_brands
    }), 200

@car_brand_bp.route('/api/car-brand', methods=['POST'])
def create_car_brand():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"status": "error", "message": "Name is required"}), 400
    car_brand = add_car_brand(name)
    return jsonify({
        "status": "success",
        "data": car_brand
    }), 201

@car_brand_bp.route('/api/car-brand/<int:brand_id>', methods=['PUT'])
def update_car_brand_by_id(brand_id):
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"status": "error", "message": "Name is required"}), 400
    updated_car_brand = update_car_brand(brand_id, name)
    if updated_car_brand:
        return jsonify({"status": "success", "data": updated_car_brand}), 200
    return jsonify({"status": "error", "message": "Car brand not found"}), 404

@car_brand_bp.route('/api/car-brand/<int:brand_id>', methods=['DELETE'])
def delete_car_brand_by_id(brand_id):
    if delete_car_brand(brand_id):
        return jsonify({"status": "success", "message": "Car brand deleted"}), 200
    return jsonify({"status": "error", "message": "Car brand not found"}), 404

# Endpoint untuk Price
@car_brand_bp.route('/api/prices', methods=['GET'])
def get_all_prices():
    prices = get_prices()
    return jsonify({
        "status": "success",
        "data": prices
    }), 200

@car_brand_bp.route('/api/price', methods=['POST'])
def create_price():
    data = request.get_json()
    amount = data.get('amount')
    currency = data.get('currency')
    brand_id = data.get('brand_id')

    if not all([amount, currency, brand_id]):
        return jsonify({"status": "error", "message": "Amount, currency, and brand_id are required"}), 400
    
    price = add_price(amount, currency, brand_id)
    return jsonify({
        "status": "success",
        "data": price
    }), 201

@car_brand_bp.route('/api/price/<int:price_id>', methods=['PUT'])
def update_price_by_id(price_id):
    data = request.get_json()
    amount = data.get('amount')
    currency = data.get('currency')
    updated_price = update_price(price_id, amount, currency)
    if updated_price:
        return jsonify({"status": "success", "data": updated_price}), 200
    return jsonify({"status": "error", "message": "Price not found"}), 404

@car_brand_bp.route('/api/price/<int:price_id>', methods=['DELETE'])
def delete_price_by_id(price_id):
    if delete_price(price_id):
        return jsonify({"status": "success", "message": "Price deleted"}), 200
    return jsonify({"status": "error", "message": "Price not found"}), 404

# Endpoint untuk Production
@car_brand_bp.route('/api/productions', methods=['GET'])
def get_all_productions():
    productions = get_productions()
    return jsonify({
        "status": "success",
        "data": productions
    }), 200

@car_brand_bp.route('/api/production', methods=['POST'])
def create_production():
    data = request.get_json()
    location = data.get('location')
    year = data.get('year')
    brand_id = data.get('brand_id')

    if not all([location, year, brand_id]):
        return jsonify({"status": "error", "message": "Location, year, and brand_id are required"}), 400
    
    production = add_production(location, year, brand_id)
    return jsonify({
        "status": "success",
        "data": production
    }), 201

@car_brand_bp.route('/api/production/<int:production_id>', methods=['PUT'])
def update_production_by_id(production_id):
    data = request.get_json()
    location = data.get('location')
    year = data.get('year')
    updated_production = update_production(production_id, location, year)
    if updated_production:
        return jsonify({"status": "success", "data": updated_production}), 200
    return jsonify({"status": "error", "message": "Production not found"}), 404

@car_brand_bp.route('/api/production/<int:production_id>', methods=['DELETE'])
def delete_production_by_id(production_id):
    if delete_production(production_id):
        return jsonify({"status": "success", "message": "Production deleted"}), 200
    return jsonify({"status": "error", "message": "Production not found"}), 404
