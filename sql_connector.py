
import mysql.connector
# import the mysql.connector module from python to begin with
mydb = mysql.connector.connect(
    host="", user="", passwd="", database="")
# enter the credentials to connect to MySql Workbench
mycursor = mydb.cursor()
# initialise a cursor to fetch the data from the database
mycursor.execute(
    "")
# enter the sql query that needs to be executed
result = mycursor.fetchone()
# fetchone() method allows you to fetch the specified data from the database
print(result)
# the fetched result is printed in the terminal
