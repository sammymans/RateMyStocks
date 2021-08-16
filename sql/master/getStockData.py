
import pandas_datareader.data as web
import datetime

import pandas as pd

import mysql.connector

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

i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i], 'yahoo', startdate, enddate)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        if i == 0:
            df.to_csv(path_out+file_out)
            print (i, symbol[i],'has data stored to csv file')
            i=i+1
        else:
            df.to_csv(path_out+file_out,mode = 'a',header=False)
            print (i, symbol[i],'has data stored to csv file')
            i=i+1
    except:
        print("No information for symbol or file is open in Excel:")
        print (i,symbol[i])
        i=i+1

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

# Make a table in SQL where we will store our data from the csv



            

