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