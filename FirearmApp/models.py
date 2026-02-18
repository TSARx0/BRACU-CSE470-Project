import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="sql5.freesqldatabase.com",
            user="sql5817404",
            password="sdUcPx1JPS",
            database="sql5817404",
            port=3306
        )
        self.cursor = self.db.cursor(dictionary=True)

    def check_login(self, username, password):
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        self.cursor.execute(query, (username, password))
        return self.cursor.fetchone()

    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()
