import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='localhost123',
    database='betting_minion')

mycursor = db.cursor()
