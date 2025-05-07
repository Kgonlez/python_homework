import sqlite3

conn= sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

print("\nTask 1: Complex JOINs with Aggregation")

query = """
SELECT
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    order_id, total_price = row
    print(f"Order ID: {order_id}, Total Price: ${total_price: .2f}")

print("\nTask 2: Understanding Subqueries")

query2 = """
SELECT
    c.customer_name,
    AVG(order_totals.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT
        o.customer_id AS customer_id_b,
        o.order_id,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS order_totals
ON c.customer_id = order_totals.customer_id_b
GROUP BY c.customer_id
ORDER BY average_total_price DESC;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

for row in results2:
    customer_name, avg_total_price = row
    if avg_total_price is not None:
        print(f"{customer_name}: ${avg_total_price: .2f}")
    else:
        print(f"{customer_name}: No orders")

try:
    print("\nTask 3: An Insert Transaction Based on Data")

    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]

    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name ='Harris'")
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, 10)
        """, (order_id, product_id))

    conn.commit()

    cursor.execute("""
        SELECT l.line_item_id, l.quantity, p.product_name
        FROM line_items l
        JOIN products p ON l.product_id = p.product_id
        WHERE l.order_id = ?
    """, (order_id,))
    results = cursor.fetchall()

    print("Line Items for new order:")
    for row in results:
        print(f"Line Item ID: {row[0]}, Quantity: {row[1]}, Product: {row[2]}")

except Exception as e:
    conn.rollback()
    print("Error during transaction:", e)

print("\nTask 4: Aggregation with HAVING")

query4 = """
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) >5
ORDER BY order_count DESC;
"""

cursor.execute(query4)
results4 = cursor.fetchall()

for row in results4:
    emp_id, first_name, last_name, order_count = row
    print(f"{emp_id}: {first_name} {last_name} - {order_count} orders")

conn.close()