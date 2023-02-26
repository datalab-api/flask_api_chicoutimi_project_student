
DROP TABLE IF EXISTS product;

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    in_stock BOOLEAN NOT NULL,
    descriptions TEXT NOT NULL,
    price float NOT NULL,
    weight float NOT NULL,
    image TEXT NOT NULL,
);

insert into product (name, in_stock, descriptions, price, weight, image)
values (?,?,?,?,?,?),("Brown eggs",true,"Raw organic brown eggs in a basket",28.1,400,"0.jpg")

insert into product (name, in_stock, descriptions, price, weight, image)
values (?,?,?,?,?,?),("Sweet fresh stawberry",true,"Sweet fresh stawberry on the wooden table",29.45,299,"1.jpg")


CREATE TABLE order (    
    id INTEGER PRIMARY KEY ,
    total_price INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    credit_card VARCHAR(255) NOT,
    credit_card_   TEXT,
    shipping_information VARCHAR(255) ,
    paid BOOLEAN ,
    transaction VARCHAR(255) NOT NULL,
    shipping_price  INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (id, quantity) REFERENCES product(id)
)

