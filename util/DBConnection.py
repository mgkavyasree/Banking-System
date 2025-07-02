import mysql.connector

class DBConnection:
    @staticmethod
    def GetConnection():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kavya",
            database="hmbank"
        )
        if connection.is_connected():
            print("connected to database")
        return connection
