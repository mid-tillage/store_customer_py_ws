from flask import jsonify, request
from product_on_sale.models import ProductOnSale

def get_products_on_sale():
    products = ProductOnSale.find_all()

    serialized_products = [{'title': product.title,
                            'product': product.product,
                            'catalog': product.catalog,
                            'price': product.price,
                            'sale_start_datetime': product.sale_start_datetime,
                            'sale_end_datetime': product.sale_end_datetime} 
                            for product in products]
    
    return jsonify(serialized_products)

def create_product_on_sale():
    data = request.json

    # Extract data from request
    title = data.get('title')
    product_name = data.get('product', {}).get('name')
    product_description = data.get('product', {}).get('description')
    sale_start_datetime = data.get('sale_start_datetime')
    sale_end_datetime = data.get('sale_end_datetime')
    enterprise_name = data.get('product', {}).get('enterprise', {}).get('name')
    catalog_name = data.get('catalog', {}).get('name')
    price = data.get('price')

    # Create ProductOnSale document
    ProductOnSale.create(
        title=title,
        product_name=product_name,
        product_description=product_description,
        price=price,
        sale_start_datetime=sale_start_datetime,
        sale_end_datetime=sale_end_datetime,
        enterprise_name=enterprise_name,
        catalog_name=catalog_name
    )

    return jsonify({'message': 'Product on sale created successfully'}), 201
