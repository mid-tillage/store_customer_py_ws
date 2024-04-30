import os
from flask.cli import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(f'mongodb://{os.getenv("MONGODB_HOST")}:{os.getenv("MONGODB_PORT")}/')
db = client[os.getenv("MONGODB_NAME")]

class Catalog:
    def __init__(self, name):
        self.name = name

class Enterprise:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, name, description, enterprise):
        self.name = name
        self.description = description
        self.enterprise = enterprise

class ProductOnSale():
    def __init__(self, title, product, catalog, price, sale_start_datetime, sale_end_datetime):
        self.title = title
        self.price = price
        self.sale_start_datetime = sale_start_datetime
        self.sale_end_datetime = sale_end_datetime
        self.product = product
        self.catalog = catalog

    @staticmethod
    def find_all():
        products = db["ProductOnSale"].find()
        product_list = []
        for product in products:
            product.pop("_id", None)
            product_list.append(ProductOnSale(**product))
        return product_list
    
    @staticmethod
    def find_by_title(title):
        products = db["ProductOnSale"].find({'title': title})
        print(products)
        product_list = []
        for product in products:
            product.pop("_id", None)
            product_list.append(ProductOnSale(**product))
        return product_list

    @staticmethod
    def create(title, product_name, product_description, price, sale_start_datetime, sale_end_datetime, enterprise_name, catalog_name):
        enterprise = Enterprise(name=enterprise_name)
        enterprise_dict = enterprise.__dict__
        product = Product(name=product_name, description=product_description, enterprise=enterprise_dict)
        product_dict = product.__dict__
        catalog = Catalog(name=catalog_name)
        catalog_dict = catalog.__dict__
        product_on_sale = ProductOnSale(title=title, product=product_dict, catalog=catalog_dict, price=price, sale_start_datetime=sale_start_datetime, sale_end_datetime=sale_end_datetime)
        # Insert into MongoDB
        # db["ProductOnSale"].insert_one(product_on_sale.__dict__)

        result = db["ProductOnSale"].insert_one(product_on_sale.__dict__)
        product_on_sale._id = result.inserted_id
        return product_on_sale
        