import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3306
        )
        return conn
    except mysql.connector.Error as err:
        print("Database connection error:",err)
        return None

def create_database():
    conn=create_connection()

    if conn is None:
        return

    cursor=conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    cursor.execute("USE student_db")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb(
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT,
            course VARCHAR(100),
            marks FLOAT
        )
    """)

    print("Database and table are ready!")

    cursor.close()
    conn.close()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db",
        port=3306
    )
