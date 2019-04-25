""" This Python file contains the method for the database object classes
    and methods used in testing

    Scripted by: Rob Marchetti
    Date: May 1, 2018
    Version: 1.0,0
"""
import configparser
import pyodbc

# config stuff here
parser = configparser.ConfigParser()
parser.read(r'..\..\config\config.ini')
sql_file_path = parser.get('sql_section', 'sql_location')


def db_curr(sql_str):
    # Database Connection
    connStr = "DRIVER={SQL Server};SERVER=your_server;DATABASE=your_db;autocommit=True"
    conn = pyodbc.connect(connStr)


    # Cursor to execute the SQL QUERY
    cursor = conn.cursor()
    with open(sql_file_path + "\\" + sql_str,"r") as fd:
        sqlFile = fd.read()
        fd.close()

    # Execute the query to get data
    results = cursor.execute(sqlFile)
    return results # Returns cursor Object


