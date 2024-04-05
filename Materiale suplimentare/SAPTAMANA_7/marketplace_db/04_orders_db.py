"""
Interactiunea cu tabelul orders + tabelul order_items
"""
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CREATE ORDER

# pentru a crea o comanda completa, avem nevoie de
# un order, iar apoi avem nevoie de order items,
# care includ produsele/caracteristicile produselor

# 1. cream o comanda
order_query = """
INSERT INTO orders (customer_id, order_date)
VALUES (1, '03.07.2023');
"""

cursor.execute(order_query)
connection.commit()

# 2. adaugam linii de comanda
# order_items_query = """
# INSERT INTO order_items (order_id, product_id, quantity, total_price)
# VALUES (?, ?, ?, ?);
# """
#
# order_items = [
#     (1, 1, 2, 240),
#     (1, 2, 1, 56.99)
# ]
#
# cursor.executemany(order_items_query, order_items)
# connection.commit()

query = """
INSERT INTO order_items (order_id, product_id, total_price)
VALUES (1, 3, 25.45);
"""
cursor.execute(query)
connection.commit()

# READ/GET ORDER BY ID
get_order = """
    SELECT * FROM orders
    WHERE id = 2
    """
cursor.execute(get_order)
order = cursor.fetchone()
print(order)

# READ/GET ALL ORDERS
get_all_orders = """
    SELECT * FROM orders
    """
cursor.execute(get_all_orders)
orders = cursor.fetchall()
print(orders)

# UPDATE ORDER
cursor.execute(
    """
    UPDATE orders SET order_date = '05.04.2024'
    WHERE id = 4
    """
)
connection.commit()

"""DELETE ORDER
TEMA:
- Ce se intampla daca stergem un order? Sunt sterse automat
si order items asociate?"""
cursor.execute(
    """
    DELETE FROM orders
    WHERE id > 4
    """
)
connection.commit()
