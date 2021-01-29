import sqlite3

class Management:

    def __init__(self):
        try:
            self.db = sqlite3.connect('./database.db')
        except sqlite3.Error as e:
            print(type(e).__name__)

    def createTable(self):
        """Creates Table if it doesn't already exist in the database and adds the initial value to the table"""
        try:
            self.db.execute('CREATE TABLE IF NOT EXISTS DATA (DATE DATE PRIMARY KEY UNIQUE, WORK NUMERIC, WASTE NUMERIC)')
            self.db.execute('INSERT INTO DATA VALUES (\'2021-01-01\', 10, 2)')
            self.db.commit()
        except sqlite3.Error as e:
            print(type(e).__name__)
    
    def printTable(self):
        """"Prints all the rows that exist in the table"""
        try:
            for row in self.db.execute('SELECT * FROM DATA'):
                print(row)
        except sqlite3.Error as e:
            print(type(e).__name__)
    
    def insertData(self, data):
        """Inserts the data into the database"""
        try:
            self.db.execute('INSERT INTO DATA VALUES (\'{}\', {}, {})'.format(data[0], data[1], data[2]))
            self.db.commit()
        except sqlite3.Error as e:
            print(type(e),__name__)
    
    def returnData(self):
        """Returns the data from the database"""
        try:
            data = []
            for row in self.db.execute('SELECT * FROM DATA'):
                data.append(list(row))
            return data
        except sqlite3.Error as e:
            print(type(e),__name__)