import mysql.connector as sql

#connect to the database
db = sql.connect(host = "localhost", user= "root", passwd="050893", database = "pysql")

#create a cursor for the DB
cursor = db.cursor()

try:
    cursor.execute("alter table pytable alter ID NOT NULL")
    print("gumtha")

except:
    print("iyayooooooooooooo")
