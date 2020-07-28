
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="4675", database="info")
mycursor = mydb.cursor()
mycursor.execute(
    "select book_name from book_info where book_author = 'Anupam' ")
result = mycursor.fetchone()
print(result)
