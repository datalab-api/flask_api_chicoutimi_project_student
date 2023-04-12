CREATE DATABASE api8inf349;

create schema extensions;

-- make sure everybody can use everything in the extensions schema
grant usage on schema extensions to public;

grant execute on all functions in schema extensions to public;

-- include future extensions
alter default privileges in schema extensions grant execute on functions to public;

alter default privileges in schema extensions grant usage on types to public;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" schema extensions;

set
    search_path = extensions;

DROP TABLE IF EXISTS product;

DROP TABLE IF EXISTS credit_card;

DROP TABLE IF EXISTS shipping_information;

DROP TABLE IF EXISTS credit_card;

DROP TABLE IF EXISTS transactions;

DROP TABLE IF EXISTS order;

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    in_stock TEXT NOT NULL,
    descriptions TEXT NOT NULL,
    price TEXT NOT NULL,
    weight TEXT NOT NULL,
    image TEXT NOT NULL
);

CREATE TABLE create_table_shipping_information (
    country TEXT PRIMARY KEY, 
    address TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL
);

CREATE TABLE credit_card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    first_digits TEXT NOT NULL,
    last_digits TEXT NOT NULL,
    expiration_year INTEGER NOT NULL,
    expiration_month INTEGER NOT NULL
);

CREATE TABLE transactions (
    id TEXT PRIMARY KEY,
    success TEXT NOT NULL,
    amount_charged TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    total_price INTEGER NOT NULL,
    email TEXT NOT NULL,
    credit_card TEXT ,
    shipping_information TEXT,
    paid TEXT ,
    transactions TEXT NOT NULL,
    shipping_price  INTEGER NOT NULL,
    quantity INT NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

