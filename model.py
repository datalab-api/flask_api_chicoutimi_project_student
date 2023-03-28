#!/usr/bin/env python3
import os
import json
import psycopg2
from psycopg2 import Error


headers = ["id","name","in_stock","descriptions","price","weight","image"]


def connect_to_db ():
    try:
        conn = psycopg2.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"))
        return conn
    except (Exception, Error) as error:
        return ("Error while connecting to PostgreSQL", error)


def drop_table(table_name):
    try:
        conn = connect_to_db()
        conn.execute("DROP TABLE IF EXISTS {}".format(table_name))
        print("Table {} dropped".format(table_name))
    except:
        print("Table {} does not exist".format(table_name))
    finally:
        conn.close()


def init_product_db():
    products = []
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        
        sql_string = "INSERT INTO product (name, in_stock, descriptions, price, weight, image) VALUES (?,?,?,?,?,?)"
        sql_value1 = ('Brown eggs','true', 'Raw organic brown eggs in a basket','28','400','0.jpg')
        sql_value2 = ('Sweet fresh strawberry', 'true','Sweet fresh strawberry on the wooden table','29.45','299','1.jpg')
        cur.execute(sql_string,sql_value1)
        cur.execute(sql_string,sql_value2)      
        conn.commit()
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
        print("Error in init_db")
    finally:
        conn.close()
        
    return products        

    
def create_table_product ():
    try:
        conn = connect_to_db()
        conn.execute("CREATE TABLE product ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, in_stock TEXT NOT NULL, descriptions TEXT NOT NULL, price TEXT NOT NULL, weight TEXT NOT NULL, image TEXT NOT NULL)")
        
        conn.commit()        
        print("Table product created ")
    except:
        print("Product table creation failed - Maybe table")
        
    finally:
        conn.close()


# create table of shipping_information
def create_table_shipping_information():
    try:
        conn = connect_to_db()
        conn.execute("CREATE TABLE shipping_information (country TEXT PRIMARY KEY, address TEXT NOT NULL, postal_code TEXT NOT NULL, city TEXT NOT NULL, province TEXT NOT NULL)")
        
        conn.commit()        
        print("Table Shipping_information created ")
    except:
        print("Shipping_information table creation failed - Maybe table")
        
    finally:
        conn.close()

# create table of credit_card
def create_table_credit_card():
    try:
        conn = connect_to_db()
        conn.execute("CREATE TABLE credit_card (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, first_digits TEXT NOT NULL, last_digits TEXT NOT NULL, expiration_year INTEGER NOT NULL,expiration_month INTEGER NOT NULL)")
        
        conn.commit()        
        print("Table Credit_card created ")
    except:
        print("Credit_card table creation failed - Maybe table")
        
    finally:
        conn.close()


# create table of transaction
def create_table_transaction():
    try:
        conn = connect_to_db()
        conn.execute("CREATE TABLE transactions (id TEXT PRIMARY KEY, success TEXT NOT NULL, amount_charged TEXT NOT NULL)")
        
        conn.commit()        
        print("Table of transactions created ")
    except:
        print("Transactions of  table creation failed - Maybe table")
        
    finally:
        conn.close()



def create_table_order():
    try:
        conn = connect_to_db()
        conn.execute('CREATE TABLE orders (id INTEGER PRIMARY KEY,total_price INTEGER NOT NULL,email TEXT NOT NULL,credit_card TEXT , shipping_information TEXT,paid TEXT ,transactions TEXT NOT NULL,shipping_price  INTEGER NOT NULL,quantity INT NOT NULL,product_id INTEGER NOT NULL, FOREIGN KEY (product_id) REFERENCES product(id))')
        conn.commit()        
        print("Table Order created ")
    except:
        print("Order table creation failed - Maybe table")
        
    finally:
        conn.close()



def insert_table(table_name, data):
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


# delete table from database 
for table_name in ["product","credit_card","shipping_information","credit_card","transactions","order"]:
    drop_table(table_name)



# create table in database
create_table_product()
create_table_shipping_information()
create_table_credit_card()
create_table_transaction()
create_table_order()
response=init_product_db()
print(response)