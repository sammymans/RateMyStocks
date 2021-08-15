import mysql.connector
from mysql.connector import Error
import pandas as pd

# function to create a connection to the SQL server
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    # try-except block to handle any errors
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            # added this after, need for connecting to database
            database = db_name
        )
        # Print success message if a connection is secured
        print("---MySQL Database connection successful---")
    except Error as err:
        print(f"Error: '{err}'")
    
    # if successful, return
    return connection

connection = create_server_connection("localhost", "root", "SammySQL@7s", "")

# takes two arguments, the connection and SQL query
def create_database(connection, query):

    # use cursor method to create cursor object --> has many useful methods, like execute
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("---Database created successfully---")
    except Error as err:
        print(f"Error: '{err}'")

# Let's make a database called stockdata
create_database_query = "CREATE DATABASE stockdata"
create_database(connection, create_database_query)

def execute_query(connetion, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # commit is used to ensure commands detailed in SQL queries are implemented
        connection.commit()
        print("query succesful")
    except Error as err:
        print(f"Error: '{err}'")

create_stocks_table = """
CREATE TABLE stocks(
    date DATE, 
    high DECIMAL(15,2),
	low DECIMAL(15,2), 
    open DECIMAL(15,2), 
    close DECIMAL(15,2), 
    volume DECIMAL(15,1),
    adjClose DECIMAL(15,2)
)
"""

# make a connection to the database
connection = create_server_connection("localhost", "root", "SammySQL@7s", "stockdata")
# execute the defined query
execute_query(connection, create_stocks_table)

populate_stocks = """
INSERT INTO stocks VALUES
('2021-01-01', 1,2,3,4,5,6),
('2021-01-01', 1,2,3,4,5,6),
('2021-01-01', 1,2,3,4,5,6),
('2021-01-01', 1,2,3,4,5,6)
"""
connection = create_server_connection("localhost", "root", "SammySQL@7s", "stockdata")
# execute the defined query
execute_query(connection, populate_stocks)