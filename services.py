
#!/usr/bin/env python3
import json
#14
from flask import Flask, jsonify
import sqlite3

from .model import headers, connect_to_db
app = Flask(__name__)
#Add product

def add_product(table_name, data):
    insert_product= {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        #sql_string = f'INSERT INTO product (name, in_stock, descriptions, price, weight, image) \
        #    VALUES ("{data["name"]}", "{data["in_stock"]}", "{data["descriptions"]}", "{data["price"]}","{data["weight"]}","{data["image"]}");'

        #cur.execute(sql_string)

        sql_string = "INSERT INTO product (name, in_stock, descriptions, price, weight, image) VALUES (?,?,?,?,?,?)"
        sql_data = (data['name'], data['in_stock'], data['descriptions'], data['price'], data['weight'], data['image'])
        print("insert data : {}".format(data))
        cur.execute(sql_string,data)        
        conn.commit()
        
        response_body = {
            'response': {
                'status': 'OK',
                'file': data
            }
	    }
        insert_product = json.dumps(response_body)

    except :
        conn.rollback()
    finally:
        conn.close()
    return insert_product

#Get_product_by_id

def get_product_by_id (id):
    product = {}    
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        #print("get product by id : {}".format(id))
        row = conn.execute("SELECT * FROM product WHERE id = {}".format(id)).fetchone()
        index = row
        i = 0
        for j in index:
            product[headers[i]] = j
            #print(headers[i]+": {}".format(product[headers[i]]))
            i+=1        
    except:
        product = {}

    return product

#Get_products

def get_products():
    products = []
    try:
        conn = connect_to_db()
        rows = conn.execute("SELECT * FROM product").fetchall()        
        for item in rows:
            product = {}

            index = item
            i = 0
            for j in index:
                product[headers[i]] = j
                #print(headers[i]+": {}".format(product[headers[i]]))
                i+=1
            products.append(product)  
    except :
        products = []
    return products



def add_order(order):
    response = {}
    return response



#api_get_order_by_id (14)

@app.route('/api/v1/orders/<int:id>', methods=['GET'])
def api_get_orders(id):
    # récupérer les informations de commande de la base de données ou d'un autre endroit
    order_info = {
        "order": {
            "id": 6543,
            "total_price": 9148,
            "email": None,
            "credit_card": {},
            "shipping_information": {},
            "paid": False,
            "transaction": {},
            "product": {
                "id": 123,
                "quantity": 1
            },
            "shipping_price": 1000
        }
    }
    # filtrer les informations de commande pour ne retourner que celles correspondant à l'ID de la commande demandée
    order = order_info.get("order", {})
    if order.get("id") != id:
        return jsonify({"error": "Order not found"}), 404
    
    return jsonify(order), 200

#Add_order


def add_orders(table_name, data):
    # Connexion à la base de données
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()

    # Construction de la requête SQL d'insertion
    query = f"INSERT INTO {table_name} (id, total_price, email, credit_card, shipping_information, paid, transaction, product_id, product_quantity, shipping_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (
        data['order']['id'], 
        data['order']['total_price'], 
        data['order']['email'], 
        str(data['order']['credit_card']), 
        str(data['order']['shipping_information']), 
        data['order']['paid'], 
        str(data['order']['transaction']), 
        data['order']['product']['id'], 
        data['order']['product']['quantity'], 
        data['order']['shipping_price']
    )

    # Exécution de la requête
    cursor.execute(query, values)

    # Validation de la transaction
    conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()

