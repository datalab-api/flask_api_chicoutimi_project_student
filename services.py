#!/usr/bin/env python3
import json
import os
from flask import Flask, jsonify
import psycopg2
from psycopg2 import Error


headers = ["id","name","in_stock","descriptions","price","weight","image"]

# function to connect
def connect_to_db ():
    try:
        conn = psycopg2.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"))
        return conn
    except (Exception, Error) as error:
        return ("Error while connecting to PostgreSQL", error)

# function to drop table
def drop_table(table_name):
    try:
        conn = connect_to_db()
        conn.execute("DROP TABLE IF EXISTS {}".format(table_name))
        print("Table {} dropped".format(table_name))
    except:
        print("Table {} does not exist".format(table_name))
    finally:
        conn.close()


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



#get_order_by_id (14)

def get_orders_by_id(id):
    orders = {}    
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        #print("get orders by id : {}".format(id))
        row = conn.execute("SELECT * FROM orders WHERE id = {}".format(id)).fetchone()
        index = row
        i = 0
        for j in index:
            #orders[headers_orders[i]] = j
            #print(headers[i]+": {}".format(orders[headers[i]]))
            i+=1        
    except:
        orders = {}

    return orders

#Add Orders
def add_orders(table_name, data):
    insert_orders= {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        #sql_string = f'INSERT INTO product (name, in_stock, descriptions, price, weight, image) \
        #    VALUES ("{data["name"]}", "{data["in_stock"]}", "{data["descriptions"]}", "{data["price"]}","{data["weight"]}","{data["image"]}");'

        #cur.execute(sql_string)
        price = conn.execute("SELECT price FROM product WHERE id = {}".format(data['product_id'])).fetchone()
        total_price = data['product_quantity']*price

        
        sql_string = "INSERT INTO orders (id, total_price, email, credit_card, shipping_information, paid, transaction, product_id, product_quantity, shipping_price) VALUES (?,?,?,?,?,?,?,?,?,?)"
        sql_data = (data['id'], total_price, data['email'], data['credit_card'], data['shipping_information'], data['paid'], data['transaction'], data['product_id'], data['product_quantity'], data['shipping_price'])
        print("insert data : {}".format(data))
        cur.execute(sql_string,data)        
        conn.commit()
        
        response_body = {
            'response': {
                'status': 'OK',
                'file': data
            }
	    }
        insert_orders = json.dumps(response_body)

    except :
        conn.rollback()
    finally:
        conn.close()
    return insert_orders

#Get_orders

def get_orders():
    orders = []
    try:
        conn = connect_to_db()
        rows = conn.execute("SELECT * FROM orders").fetchall()        
        for item in rows:
            order = {}

            index = item
            i = 0
            for j in index:
                order[headers_orders[i]] = j
                #print(headers[i]+": {}".format(product[headers[i]]))
                i+=1
            orders.append(order)  
    except :
        orders = []
    return orders