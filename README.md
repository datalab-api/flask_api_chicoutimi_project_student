Title
===
Abstract:xxx
## Papar Information
- Title:  `me`
- Authors:  `A`
- Preprint: [https://arxiv.org/abs/xx]()


## Install & Dependence
- python3
- Flask
- Sqlite



## Use
- for install dependancies
  ```bash
  pip3 install -r requiremments.txt

  ```
- for init database
  ```
  python3 model.py
  ```
- for create var env
  ```
  export FLASK_DEBUG=1
  export FLASK_ENV=development  
  ```


## Description Model API
ce table il epermet 
```
CREATE TABLE order (    
    id INTEGER PRIMARY KEY ,
    total_price INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    credit_card VARCHAR(255) NOT,
    credit_card_   TEXT,
    shipping_information VARCHAR(255) ,
    paid BOOLEAN ,
    transactions VARCHAR(255) NOT NULL,
    shipping_price  INT NOT NULL,
    quantity INT NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_product) REFERENCES product(id)
)  
  ```


## Description services API


## References
- [code-1](https://github.com)
- [code-2](https://github.com)
  
## License

## Citing
If you use xxx,please use the following BibTeX entry.
```
```
