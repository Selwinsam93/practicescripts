import mysql.connector as sql

try:
    db = sql.connect(host="localhost", user="root",passwd="050893")
    print("Connection successful")

except:
    print("Oops something happend!!!")
