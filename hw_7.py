# import sqlite3
#
#
# def create_table(db_name, create_table_sql):
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)
#
#
# db_name = '''hw.db'''
# #sql_to_create_products_table = '''
# CREATE TABLE products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_title VARCHAR(200) NOT NULL,
#     price FLOAT DEFAULT 0.0 NOT NULL,
#     quantity INTEGER DEFAULT 0 NOT NULL
# )
# '''
# def insert_products(db_name, product):
#     sql = '''INSERT INTO products (product_title, price, quantity)
#     VALUES (?, ?, ?)'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, product)
#             connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# def update_quantity(db_name, id, new_quantity):
#     sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (new_quantity, id))
#             connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# def update_price(db_name, id, new_price):
#     sql = '''UPDATE products SET price = ? WHERE id = ?'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (new_price, id))
#             connection.commit()
#     except sqlite3.Error as e:
#             print(e)
#
# def delete_product(db_name, id):
#     sql = '''DELETE FROM products WHERE id = ?'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (id,))
#             connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# def select_all_products(db_name):
#     sql = '''SELECT * FROM products'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql)
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
# def select_products_by_price_and_quantity(db_name, price_limit, quantity_limit):
#     sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (price_limit, quantity_limit))
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
# def search_products_by_name(db_name, search_name):
#     sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, ('%' + search_name + '%',))
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
#
# select_all_products(db_name)
#
# update_quantity(db_name, 1, 20)
# update_price(db_name, 1, 35)
# delete_product(db_name, 15)
# print('---------------------')
# print('Updated table:')
# select_all_products(db_name)
# print('---------------------')
# print('Products with price lower than 100 and quantity greater than 5:')
# select_products_by_price_and_quantity(db_name, 100, 5)
# print('---------------------')
# print('Searching products by name:')
# search_products_by_name(db_name, 'мыло')
#
#
#
# # my_connection = create_connection(db_name)
# # if my_connection is not None:
# #     print('Connected to database')
# #     create_table(my_connection, sql_to_create_products_table)
# #     inset_products(my_connection, ())
# #     my_connection.close()
#
# # create_table(db_name, sql_to_create_products_table)
# # insert_products(db_name, ('Мыло детское', 30, 10))
# # insert_products(db_name, ('Жидкое мыло', 100, 15))
# # insert_products(db_name, ('Молоко', 80, 20))
# # insert_products(db_name, ('Масло сливочное', 130, 10))
# # insert_products(db_name, ('Масло растительное', 180, 5))
# # insert_products(db_name, ('Кофе', 230, 8))
# # insert_products(db_name, ('Чай', 180, 10))
# # insert_products(db_name, ('Хлеб', 25, 20))
# # insert_products(db_name, ('Сигареты', 140, 60))
# # insert_products(db_name, ('Стиральный порошок', 120, 10))
# # insert_products(db_name, ('Сахар рафинированный', 90, 10))
# # insert_products(db_name, ('Салфетки влажные', 20, 25))
# # insert_products(db_name, ('Стаканчики одноразовые', 5, 100))
# # insert_products(db_name, ('Кокосовое масло', 190, 6))
# # insert_products(db_name, ('Средство для мытья посуды', 140, 17))