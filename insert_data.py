import sqlite3

def insert_sample_data():

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Insert sample user data
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                   ('Alice', 'alice@example.com', 'password123'))
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                   ('Bob', 'bob@example.com', 'password456'))

    # Insert sample category data
    cursor.execute("INSERT INTO categories (name) VALUES (?)", ('Food',))
    cursor.execute("INSERT INTO categories (name) VALUES (?)", ('Entertainment',))
    cursor.execute("INSERT INTO categories (name) VALUES (?)", ('Transport',))

    # Insert sample expense data
    cursor.execute("""
    INSERT INTO expenses (user_id, category_id, amount, description, date) 
    VALUES (?, ?, ?, ?, ?)
    """, (1, 1, 50.75, 'Lunch at cafe', '2024-12-23'))
    cursor.execute("""
    INSERT INTO expenses (user_id, category_id, amount, description, date) 
    VALUES (?, ?, ?, ?, ?)
    """, (2, 2, 100.00, 'Movie ticket', '2024-12-22'))


    connection.commit()
    connection.close()

    print("Sample data inserted successfully.")


if __name__ == "__main__":
    insert_sample_data()
