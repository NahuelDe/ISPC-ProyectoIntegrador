import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8704",
    database="DispositivosInteligentes"
)

print(midb)
