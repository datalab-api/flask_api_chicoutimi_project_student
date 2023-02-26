
#!/usr/bin/env python3
import json

from .model import headers, connect_to_db



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