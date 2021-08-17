from os import name
from pandas.core.frame import DataFrame
import pandas_datareader.data as web
import datetime

import pandas as pd

import mysql.connector

import csv

from sqlalchemy import create_engine

# First, we need to read all of the ticker symbols from the excel that I created
symbol = []
a = 'ExhangeSymbols.csv'
b = 'short_stock_symbol_list.txt'
with open(b) as f:
    for line in f:
        symbol.append(line.strip())
f.close

#print(symbol)

# Then, pick the start and end dates that we want our data to span over
#startdate = datetime.date(2009,1,1)
startdate = datetime.date(2020,1,1)
#enddate = datetime.date.today()
enddate = datetime.date(2021,1,1)

# Make a file path to where we will save our csv
# We will work with the csv and SQL

path_out = 'C:/Users/sfarn/Documents/Programming/Personal Projects/RateMyStonks/PythonToSQL/'
file_out = 'yahoo_prices_volumes_for_RateMyStonks.csv'
 
# Loop through tickers in symbol list
# If the ticker cannot be found in yahoo finance, just skip over it

# i=0
# while i<len(symbol):
#     try:
#         df = web.DataReader(symbol[i], 'yahoo', startdate, enddate)
#         df.insert(0,'Symbol',symbol[i])
#         df = df.drop(['Adj Close'], axis=1)
#         if i == 0:
#             df.to_csv(path_out+file_out)
#             print (i, symbol[i],'has data stored to csv file')
#             i=i+1
#         else:
#             df.to_csv(path_out+file_out,mode = 'a',header=False)
#             print (i, symbol[i],'has data stored to csv file')
#             i=i+1
#     except:
#         print("No information for symbol or file is open in Excel:")
#         print (i,symbol[i])
#         i=i+1

# Now that we have our csv file filled with all of the data we need...    
# Lets's Make a connection to the SQL Server

# First need to make the database in the SQL Workbench, then run the connection code (need to make in SQL first)
# Initiliaze the databse in SQL Workbench first

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="SammySQL@7s",
    database = "stockdatabase"
)

# Make a cursor based on the established connection
cursor = connection.cursor()

# Store our csv file of all of our stock data into a variable called data
data = pd.read_csv(path_out + file_out)
#print(data)

# Change csv into pandas dataframe
df = DataFrame(data, columns=['Date','Symbol','High','Low','Open','Close','Volume'])
#print(df)

# Make a table in SQL where we will store our data from the csv
# cursor.execute("""CREATE TABLE yahoo_prices_for_stocks (
#     Date date,
#     Symbol nvarchar(5),
#     High decimal(15,2),
#     Low decimal(15,2),
#     Open decimal(15,2),
#     Close decimal(15,2),
#     Volume int
# )"""
# )

#-----------------------------------------------------
# At this stage, we have a csv created with all of the stock information
# With the csv file, we have also made a pandas dataframe with all of the same information
# We have also created an SQL table, that is in a database initialized in SQL Workbench
# All that is left is too finally add the data, either from the csv or pandas dataframe, to the SQL table
#-----------------------------------------------------


# Finally, we need to insert rows from our csv file into our SQL Table

for i, row in df.iterrows():
    sql = """ INSERT INTO yahoo_prices_for_stocks (Date, Symbol, High, Low, Open, Close, Volume)
    VALUES (%s,%s,%s,%s,%s,%s,%s);
    """
    cursor.execute(sql, tuple(row))
    connection.commit()






            

