"""
Interactiunea cu tabelul products
"""
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

"""CRUD

CREATE PRODUCT"""
# product_query = """
# INSERT INTO products (name, category, price, stock_count, description)
# VALUES (?, ?, ?, ?, ?);
# """
#
# products = [
#     ("birou negru", "mobilier", 120, 2, "birou negru descriere"),
#     ("pitic de gradina", "gradina", 56.99, 5, "pitic gradina descriere"),
#     ("ghiveci flori alb", "gradina", 25.45, 10, "ghiveci flori descriere")
# ]
#
# cursor.executemany(product_query, products)
# connection.commit()


"""READ PRODUCT (BY ID)"""
# read_product_by_id = """
#     SELECT *
#     FROM products
#     WHERE id = ?
#     """
#
# cursor.execute(read_product_by_id, (2,))
# product_2 = cursor.fetchone()
# print(product_2)

"""READ/GET ALL PRODUCTS"""
read_all_products = """
    SELECT description
    FROM products
    ORDER BY name DESC
    """
cursor.execute(read_all_products)
all_products = cursor.fetchall()
print(all_products)

"""UPDATE PRODUCT"""
cursor.execute("""
    UPDATE products SET name = 'birou wenge', price = 780
    WHERE id = 1
""")

connection.commit()

"""DELETE PRODUCT"""
cursor.execute("""
    DELETE FROM products
    WHERE id = 6
    """)
connection.commit()
