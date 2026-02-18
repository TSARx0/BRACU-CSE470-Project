import mysql.connector

# Connect to your online database
db = mysql.connector.connect(
    host="sql5.freesqldatabase.com",
    user="sql5817404",
    password="sdUcPx1JPS",
    database="sql5817404",
    port=3306
)

cursor = db.cursor()
cursor.execute("SHOW TABLES")
for table in cursor.fetchall():
    print(table)

input("👍")


db.close()

