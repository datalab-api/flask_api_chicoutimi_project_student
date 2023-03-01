#!/usr/bin/env python3
import sqlite3, json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from .model import headers, connect_to_db
from .services import (add_product, get_product_by_id, get_products, add_orders, api_get_orders)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# ENDPOINT PRODUCT 
# endpoint product 
@app.route("/", methods=['GET'])
def api_product_all():
    return Response(json.dumps({"products": get_products()}),
                        status=200, mimetype='application/json')

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def api_get_products(id):
    return Response(json.dumps(get_product_by_id(id)),
                        status=200, mimetype='application/json')

# methode d'api qui permet d'ajouter un product 
@app.route('/api/v1/product/add', methods=['POST'])
def api_add_product():
    product = request.get_json()
    return Response(json.dumps(add_product("product", product)),
                        status=200, mimetype='application/json')



# ENDPOINT ORDER
#methode d'api get_by_orders (14)

@app.route('/api/v1/orders/<int:id>', methods=['GET'])
def api_get_orders(id):
    return Response(json.dumps(api_get_orders(id)),
                        status=200, mimetype='application/json')
# methode d'api qui permet d'ajouter un orders 
@app.route('/api/v1/orders/add', methods=['POST'])
def add_orders():
    orders = request.get_json()
    return Response(json.dumps(add_orders("orders", orders)),
                        status=200, mimetype='application/json')

@app.route('/order', methods=['POST'])
def api_add_order():
    message= {}
    status = 200
    if request.method == 'POST': 
        order = request.get_json()
        item = order['product']
        if item == None:
            status = 422
            message = '{"errors" : {"product": { "code": "missing-fields", "name": "La création d une commande nécessite un produit"}}}'
        else:
            if item['id'] == None  or item['quantity'] == None or int(item['quantity']) < 1:
                status=422
                message = '{"errors" : {"product": { "code": "missing-fields", "name": "La création d une commande nécessite un produit"}}}'
            else:
                conn = connect_to_db()
                cur = conn.cursor()
                #print("get product by id : {}".format(id))
                row = conn.execute("SELECT * FROM product WHERE id = {}".format(item['id'])).fetchone()
                
                if row == None:
                    status=422
                    message = '{"errors" : {"product": { "code": "missing-fields", "name": ""Le produit demandé n est pas en inventaire""}}}'
                else:
                    order= {}
                    product = {}
                    i = 0
                    for j in index:
                        product[headers[i]] = j
                        #print(headers[i]+": {}".format(product[headers[i]]))
                        i+=1
                    


                    message = 'ok'  

    return app.response_class(response=json.dumps(message,indent=2),status=status, mimetype='application/json')

    

if __name__ == '__main__':  # le main de l'application pour l'exécuter
    
    app.run(debug=True)   



    # env FLASK_APP=app.py python -m flask run
    # set FLASK_APP=app.py
