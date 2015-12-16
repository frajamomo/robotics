import MySQLdb
import time
from datetime import datetime

class Database:

    host = 'localhost'
    user = 'javier'
    password = 'guazala'
    db = 'Monitoring'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__=="__main__":
    db = Database()
    for i in range (1000):
        temperature = i
        humidity = i*100
        query = ("INSERT INTO TempHumid (TimeStamp, Temperature, Humidity) VALUES (NOW(), %s, %s)" % (temperature, humidity))
        db.insert(query)

