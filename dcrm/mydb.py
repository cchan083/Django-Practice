import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sop123rano#'
    
)

# prepare cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")