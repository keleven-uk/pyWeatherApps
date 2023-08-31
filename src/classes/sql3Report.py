###############################################################################################################
#    sql3Report   Copyright (C) <2023>  <Kevin Scott>                                                         #
#    stores the highs and low weather values.                                                                 #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023>  <Kevin Scott>                                                                      #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

import sqlite3
from sqlite3 import Error

from src.classes.dataClasses import weatherValues


class sql3Data():

    def __init__(self, DBname):
        self.DBname = DBname
        self.sqlConnect()

    def sqlConnect(self):
        """  Connect to a sql3lite database and create a cursor object.
             The name of the database id supplied to the class through __init__()
        """
        self.cnx = None
        try:
            #establishing the connection
            self.cnx = sqlite3.Connection(self.DBname)

            #  A lot of increase in speed.
            #  https://avi.im/blag/2021/fast-sqlite-inserts/
            # self.cnx.execute("PRAGMA journal_mode = OFF;")              #  Turns off rollback journal, thus we cannot go back if any of the transactions fail.
            # self.cnx.execute("PRAGMA synchronous = 0;")                 #  SQLite does not care about writing to disk reliably and hands off that responsibility to the OS.
            # self.cnx.execute("PRAGMA cache_size = 1000000;")            #  Specifies how many memory pages SQLite is allowed to hold in the memory.
            # self.cnx.execute("PRAGMA locking_mode = EXCLUSIVE;")        #  Locking mode, the lock held by the SQLite connection is never released.
            # self.cnx.execute("PRAGMA temp_store = MEMORY;")             #  Make it behave like an in-memory database.

            #Creating a cursor object using the cursor() method
            self.cursor = self.cnx.cursor()
        except Error as err:
            raise sqlError(err) from Error


    def execute(self, query, data=""):
        """  Execute a given SQL3lite query, with an optional data set.
        """
        try:
            self.cursor.execute(query, data)
            # Commit your changes in the database
            self.cnx.commit()
        except Error as err:
            raise sqlError(err) from Error


    def createTable(self):
        """  Creating blank table to hold a daily weather data.
        """
        sql = """CREATE TABLE DailyData(
                DateTime CHAR(20) PRIMARY KEY,
                MaxOutdoorTemperature FLOAT,
                MinOutdoorTemperature FLOAT
                )"""
        self.execute(sql)


    def insert(self, data):
        """  Insert data into a SQLite2 database.
             It calls self.execute with a pre-defined sql query and the supplied data.
        """
        query = """INSERT INTO DailyData
                   (DateTime, MaxOutdoorTemperature, MinOutdoorTemperature)
                    VALUES (?, ?)"""

        try:
            # Executing the SQL command
            self.execute(query, data)
            # Commit your changes in the database
            self.commit()
        except Error:
            self.rollback()
            raise sqlError("Insert failed, data rollback performed.") from Error


    def keyExists(self, key):
        """  Test if a given key is in the database.
             This is achieved by trying to count the instances of the key in the database.
             so, 0 is false and 1 is true.
        """
        query = "SELECT count(*) FROM DailyData WHERE DateTime = ?"
        self.execute(query, (key,))               #  Needs to be a tuple, needs the tailing comma.
        check = self.cursor.fetchone()[0]         #  Returns a tuple.
        if check == 0:
            return False
        else:
            return True


    def commit(self):
        """  Commit the changes to the sqlite3 database.
        """
        self.cnx.commit()


    def rollback(self):
        """  Rolling back in case of error
        """
        self.cnx.rollback()


    def fetchall(self):
        """  Performs a fetchall on the sqlite3database.
        """
        try:
            self.execute("SELECT * FROM DailyData ORDER BY DateTime")
            result = self.cursor.fetchall()
            return result
        except Error:
            raise sqlError("fetchall failed, has the tables been created.") from Error


    def close(self):
        """  Closing the connection
        """
        self.cnx.close()



class sqlError(Exception):
    """  A secondary class to supply custom exceptions to the SQL main class.
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"sql Error, {self.message} "
        else:
            return "sql Error has been raised"
