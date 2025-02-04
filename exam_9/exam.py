import sqlite3


def create_tables(db_name):
    sql_to_create_categories_table = '''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150) NOT NULL
    )
    '''
    sql_to_create_stores_table = '''
    CREATE TABLE IF NOT EXISTS stores (
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100) NOT NULL
    )
    '''
    sql_to_create_products_table = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(250) NOT NULL,
        category_code VARCHAR(2),
        unit_price FLOAT NOT NULL,
        stock_quantity INTEGER NOT NULL,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES stores(store_id)
    )
    '''

    try:

        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql_to_create_categories_table)
            cursor.execute(sql_to_create_stores_table)
            cursor.execute(sql_to_create_products_table)
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблиц: {e}")



def insert_category(db_name, code, title):
    sql = '''INSERT INTO categories (code, title) VALUES (?, ?)'''
    try:
        # Подключаемся к базе данных
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (code, title))
            connection.commit()
    except sqlite3.Error as e:
        print(e)



def insert_store(db_name, store_title):
    sql = '''INSERT INTO stores (title) VALUES (?)'''
    try:
        # Подключаемся к базе данных
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (store_title,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)



def insert_product(db_name, product_title, category_code, unit_price, stock_quantity, store_id):
    sql = '''INSERT INTO products (product_title, category_code, unit_price, stock_quantity, store_id) 
    VALUES (?, ?, ?, ?, ?)'''
    try:
        # Подключаемся к базе данных
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_title, category_code, unit_price, stock_quantity, store_id))
            connection.commit()
    except sqlite3.Error as e:
        print(e)



def populate_database(db_name):

    # insert_category(db_name, 'FD', 'Food products')
    # insert_category(db_name, 'CT', 'Clothing')
    # insert_category(db_name, 'HT', 'Household items')
    #
    #
    # insert_store(db_name, 'Asia')
    # insert_store(db_name, 'Globus')
    # insert_store(db_name, 'Spar')
    #
    #
    insert_product(db_name, 'Chocolate', 'FD', 10.5, 129, 1)  # Asia
    insert_product(db_name, 'Milk', 'FD', 20.0, 200, 2)  # Globus
    insert_product(db_name, 'Bread', 'FD', 1.5, 500, 3)  # Spar
    insert_product(db_name, 'Shirt', 'CT', 25.0, 100, 1)  # Asia
    insert_product(db_name, 'Jeans', 'CT', 45.0, 50, 2)  # Globus
    insert_product(db_name, 'Detergent', 'HT', 5.0, 300, 3)  # Spar
    insert_product(db_name, 'Socks', 'CT', 5.0, 200, 1)  # Asia
    insert_product(db_name, 'Toothpaste', 'HT', 3.0, 150, 2)  # Globus
    insert_product(db_name, 'Pan', 'HT', 15.0, 75, 3)  # Spar



def show_stores(db_name):
    sql = '''SELECT store_id, title FROM stores'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            stores = cursor.fetchall()
            return stores
    except sqlite3.Error as e:
        print(e)
        return []



def show_products_by_store(db_name, store_id):
    sql = '''SELECT p.product_title, c.title, p.unit_price, p.stock_quantity
             FROM products p
             JOIN categories c ON p.category_code = c.code
             WHERE p.store_id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (store_id,))
            products = cursor.fetchall()
            if products:
                for product in products:
                    print(f"Название продукта: {product[0]}")
                    print(f"Категория: {product[1]}")
                    print(f"Цена: {product[2]}")
                    print(f"Количество на складе: {product[3]}")
                    print('-' * 30)
            else:
                print("Нет продуктов в этом магазине.")
    except sqlite3.Error as e:
        print(e)


def main():
    db_name = 'exam_9.db'

#    create_tables(db_name)

    populate_database(db_name)

    while True:
        stores = show_stores(db_name)

        if not stores:
            print("Нет магазинов в базе данных.")
            break

        print(
            "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        for store in stores:
            print(f"{store[0]}. {store[1]}")

        try:
            store_choice = int(input("\nВведите id магазина (или 0 для выхода): "))
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        if store_choice == 0:
            print("Выход из программы...")
            break

        store_found = False
        for store in stores:
            if store[0] == store_choice:
                store_found = True
                show_products_by_store(db_name, store_choice)
                break

        if not store_found:
            print("Магазин с таким id не найден. Попробуйте снова.")


if __name__ == "__main__":
    main()