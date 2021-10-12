import sqlite3
from datetime import date, timedelta

class Management:

    def __init__(self):
        try:
            self.db = sqlite3.connect('../DataBase/database.db')
        except sqlite3.Error as e:
        	self.db = sqlite3.connect('DataBase/database.db')
        except sqlite3.Error as e:
            print(e)

    def createTable(self):
        """Creates Table if it doesn't already exist in the database and adds the values of past week to the table initializing it to 0"""
        try:
            self.db.execute('CREATE TABLE IF NOT EXISTS DATA (DATE DATE PRIMARY KEY UNIQUE, WORK NUMERIC, WASTE NUMERIC)')
            today = date.today()
            for i in range(7, 0, -1):
                self.db.execute('INSERT INTO DATA VALUES (\'{}\', 0, 0)'.format(str(today - i*timedelta(days=1))))
            self.db.commit()
        except sqlite3.Error as e:
            print(e)
    
    def printTable(self):
        """"Prints all the rows that exist in the table"""
        try:
            for row in self.db.execute('SELECT * FROM DATA'):
                print(row)
        except sqlite3.Error as e:
            print(e)

    def insertData(self, data):
        """
        Inserts the data into the database
        
        Parameter
        ---------
        data : list
            Contains `date`, `work hours` and `waste hours` in single list.
        
        Example
        -------
        >>> database.insertData(['2021-10-01', 0, 0])
        """
        try:
            self.db.execute('INSERT INTO DATA VALUES (\'{}\', {}, {})'.format(data[0], data[1], data[2]))
            self.db.commit()
        except sqlite3.Error as e:
            print(e)
    
    def returnData(self):
        """
        Returns the data from the database

        Return
        ------
        data : list
            Return all the data stored in database in 2D list.

        Example
        -------
        >>> database.returnData()
        [['2021-10-05', 0, 0], ['2021-10-06', 0, 0], ['2021-10-07', 0, 0], ['2021-10-08', 0, 0]]
        """
        try:
            data = []
            for row in self.db.execute('SELECT * FROM DATA'):
                data.append(list(row))
            return data
        except sqlite3.Error as e:
            print(e)
    
    def checkData(self, key):
        """
        Returns record if it exists else None
        
        Parameter
        ----------
        key : str
            The date should be in format ``yyyy-mm-dd``

        Return
        ------
        row_data : list | None

        Example
        --------
        >>> #If data exists
        >>> database.checkData('2021-10-12')
        [('2021-10-12', 0, 0)]
        >>> #If data doesn't exists
        >>> database.checkData('2021-10-23')
        []
        """
        try:
            row = self.db.execute('SELECT * FROM DATA WHERE DATE=\'{}\''.format(key))
            return row.fetchall()
        except sqlite3.Error as e:
            print(e)
    
    def updateData(self, data):
        """
        Update a single record on basis of DATE
        
        Parameter
        ---------
        data : list
            Contains `date`, `work hours` and `waste hours` in single list.
        
        Example
        -------
        >>> database.updateData(['2021-10-01', 0, 0])
        """
        try:
            self.db.execute('UPDATE DATA SET WORK={}, WASTE={} WHERE DATE=\'{}\''.format(data[1], data[2], data[0]))
            self.db.commit()
        except sqlite3.Error as e:
            print(e)
