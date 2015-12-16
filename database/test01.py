import MySQLdb




db = MySQLdb.connect("localhost","javier","password","Monitoring" )
cursor = db.cursor()

try:
    cursor.execute("""INSERT INTO TempHumid VALUES (%s,%s,%s)""", (1,1,1))
    db.commit()
except:
    db.rollback()

# show table
cursor.execute("""SELECT * FROM TempHumid; """)

print cursor.fetchall()
db.close()
