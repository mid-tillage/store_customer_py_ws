from flask import Flask, jsonify
from pymongo import MongoClient

from product_on_sale.controllers import create_product_on_sale, get_products_on_sale

app = Flask(__name__)
app.route('/product-on-sale', methods=['GET'])(get_products_on_sale)
app.route('/product-on-sale', methods=['POST'])(create_product_on_sale)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to your Flask API!'})

if __name__ == '__main__':
    app.run(port=3020)
