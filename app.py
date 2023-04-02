#!/usr/bin/env python3
import os 
import  json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import redis

from app.model import  connect_to_db
from app.services import (add_product, get_product_by_id, get_products, get_orders_by_id, get_orders)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

Redis = redis.from_url(url= os.getenv("ARG REDIS_URL"))

# ENDPOINT PRODUCT 
# endpoint product 
"cette methode permet de recuperer la liste des produits"
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
            message = Response(json.dumps(info), status=422, mimetype='application/json')
        else:
            message = Response(json.dumps(resultat), status=200, mimetype='application/json')

    return message

@app.route("/", methods=['GET'])
def api_orders_all():
    return Response(json.dumps({"products": get_orders()}),status=200, mimetype='application/json')

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

                row_order = conn.execute("SELECT * FROM order WHERE product_id = {}".format(item['id'])).fetchone()
                #print("get product by id : {}".format(id))

                if row_order != None:
                    status=422
                    message = '{"errors" : {"product": { "code": "missing-fields", "name": ""Le produit demandé est deja commandé""}}}'
                
                else:
                    if  order['email'] is None or order['shipping_information'] is None or \
                        order['shipping_information']['country'] is None or \
                        order['shipping_information']['address'] is None or \
                        order['shipping_information']['postal_code'] is None or \
                        order['shipping_information']['city'] is None or \
                        order['shipping_information']['province'] is None:
                        info = {
                            "errors": {
                                "order": {
                                    "code": "missing-fields",
                                    "name": "Il manque un ou plusieurs champs qui sont obligatoires",
                                }
                            }
                        }
                        message = Response(json.dumps(info), status=422, mimetype='application/json')
                    else:  
                        row_in_stock = conn.execute("SELECT in_stock FROM product WHERE id = {}".format(item['id'])).fetchone()
                        if row_in_stock == 'true':   

                            

                            message = Response(json.dumps({"products": get_orders()}), status=200, mimetype='application/json')
                        else:
                            info = {
                                "errors" : {
                                    "product": {
                                        "code": "out-of-inventory",
                                        "name": "Le produit demandé n'est pas en inventaire"
                                    }
                                }
                            }
                            message = Response(json.dumps(info), status=422, mimetype='application/json')
 
                        



    return message

    

if __name__ == '__main__':  # le main de l'application pour l'exécuter
    
    app.run(debug=True)   



    # env FLASK_APP=app.py python -m flask run
    # set FLASK_APP=app.py
