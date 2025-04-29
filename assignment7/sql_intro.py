import sqlite3

# === Task 2 === #
def create_tables(cursor):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
        """)
    print("Publishers table created successfully.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        );
        """)
    print("Magazines table created successfully.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE(name, address)
        );
        """)
    print("Subscribers table created successfully.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id),
            UNIQUE(subscriber_id, magazine_id)
        );
        """)
    print("Subscriptions table created successfully.")

# === Task 3 === #
def add_publisher(cursor,name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        result = cursor.fetchall()
        if result:
            publisher_id = result[0][0]
            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
        else:
            print(f"Publisher '{publisher_name}' not found.")
    except sqlite3.IntegrityError:
        print(f"Magazine'{name}' already exists.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchall():
            print(f"Subscriber '{name}' at '{address}' already exists.")
        else:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"Error inserting subscriber '{name}.")

def add_subscriptions (cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    try:
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
        subscriber = cursor.fetchall()
        if not subscriber:
           print(f"Subscriber '{subscriber_name}' not found.")
           return 
        subscriber_id = subscriber[0][0]

        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine = cursor.fetchall()
        if not magazine:
            print(f"Magazine '{magazine_name}' not found.")
            return
        magazine_id = magazine[0][0]

        #Checking if subscription already exists
        cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        count = cursor.fetchone()[0]
        if count > 0:
            print(f"Subscription for '{subscriber_name}' to '{magazine_name}' already exists.")
        else:
            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print(f"Error inserting subscription")

# === Task 1 === #
with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    print("Connected to database.")
# === Task 1 === #

    create_tables(cursor)

    add_publisher(cursor, "Conde Nast")
    add_publisher(cursor, "Hearst Communications")
    add_publisher(cursor, "Meredith Corporation")

    add_magazine(cursor, "Vogue", "Conde Nast")
    add_magazine(cursor, "Cosmopolitan", "Hearst Communications")
    add_magazine(cursor, "People", "Meredith Corporation")

    add_subscriber(cursor, "Anna Doe", "123 Main Street")
    add_subscriber(cursor, "Judith Smith", "456 Oak Avenue")
    add_subscriber(cursor, "Charlie Johnson", "789 Pine Road")

    add_subscriptions(cursor, "Anna Doe", "123 Main Street", "Vogue", "2025-12-31")
    add_subscriptions(cursor, "Judith Smith", "456 Oak Avenue", "Cosmopolitan", "2025-06-30")
    add_subscriptions(cursor, "Charlie Johnson", "789 Pine Road", "People", "2025-03-16")

    conn.commit()
    print("Database populated successfully.")

    # === Task 4 === #
    print("\nAll subscribers:")
    cursor.execute('SELECT * FROM subscribers')
    for row in cursor.fetchall():
        print(row)
    
    print("\nAll magazines sorted by name:")
    cursor.execute('SELECT * FROM magazines ORDER BY name')
    for row in cursor.fetchall():
        print(row)

    publisher_name = "Conde Nast"
    print(f"\nMagazines from publisher '{publisher_name}':")
    cursor.execute("""
        SELECT magazines.* 
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """, (publisher_name,))
    for row in cursor.fetchall():
        print(row)
    