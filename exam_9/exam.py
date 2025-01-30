import sqlite3



def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

db_name = 'exam_9.db'

sql_to_create_categories_table = '''
CREATE TABLE IF NOT EXISTS categories 
(code VARCHAR(2) PRIMARY KEY,
title VARCHAR(150) NOT NULL
)'''

sql_to_create_stores_table = '''
CREATE TABLE IF NOT EXISTS stores (
store_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100) NOT NULL
)'''

sql_to_create_products_table ='''
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(250) NOT NULL,
category_code VARCHAR(2),
unit_price FLOAT DEFAULT 0 NOT NULL,
store_id INTEGER,
FOREIGN KEY (category_code) REFERENCES categories(code),
FOREIGN KEY (store_id) REFERENCES products(id)
)'''

#create_table(db_name, sql_to_create_categories_table)
#create_table(db_name, sql_to_create_stores_table)
#create_table(db_name, sql_to_create_products_table)

def insert_category(db_name,category):
    sql = '''INSERT INTO categories (code, title) VALUES (?,?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, category)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_store(db_name, store):
    sql = '''INSERT INTO stores (title) VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, store)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_product(db_name, product):
    sql = '''INSERT INTO products (title, category_code, unit_price, store_id) VALUES (?,?,?,?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

insert_store(db_name, 'ASIA')
insert_store(db_name, 'Globus')
insert_store(db_name, 'Spar')

