
from flask import Flask
app = Flask(__name__)

from app.model import connect_to_db, headers_orders

from app.model import add_product,get_product_by_id, get_products, get_orders_by_id, add_orders, get_orders


