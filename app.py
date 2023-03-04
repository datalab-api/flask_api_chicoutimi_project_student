#!/usr/bin/env python3
import sqlite3, json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from .model import headers, connect_to_db
from .services import (add_product, get_product_by_id, get_products, get_orders_by_id, get_orders)

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

@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def api_get_orders_by_id(order_id):
    Response = {}
    resultat = get_orders_by_id(order_id)
    if order_id is None or resultat == None:
        message = Response(json.dumps({message:"Commande inexistante"}),
                        status=404, mimetype='application/json')
    else:
       
        if  resultat['email'] is None or resultat['shipping_information'] is None or \
            resultat['shipping_information']['country'] is None or \
            resultat['shipping_information']['address'] is None or \
            resultat['shipping_information']['postal_code'] is None or \
            resultat['shipping_information']['city'] is None or \
            resultat['shipping_information']['province'] is None:
            info = {
        "errors": {
            "order": {
                "code": "missing-fields",
                "name": "Il manque un ou plusieurs champs qui sont obligatoires",
            }
        }
    }
    message = Response(
        json.dumps(info), status=422, mimetype='application/json')

    return message

@app.route("/", methods=['GET'])
def api_orders_all():
    return Response(json.dumps({"products": get_orders()}),
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
                   
                    


                    message = 'ok'  

    return app.response_class(response=json.dumps(message,indent=2),status=status, mimetype='application/json')

    

if __name__ == '__main__':  # le main de l'application pour l'exécuter
    
    app.run(debug=True)   



    # env FLASK_APP=app.py python -m flask run
    # set FLASK_APP=app.py
