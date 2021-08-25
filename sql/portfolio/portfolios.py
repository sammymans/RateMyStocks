# The goal is to make an SQL Table that has a bunch of people's portfolios

# We will utilize normalization in order to achieve this :
#   One table will store the ID of a customer
#   Another table will hold the customers portfolio - this table will contain:
#       the user ID, ticker, date purchased, shares, purchase price

# Once the tables have been initilialized, populate via hardcode

# After the two tables have been constructed and populated, we want to show all the holdings, as well as some of the metrics (GIVEN THE ID):
#   holdings: stock : number of shares --> what is the current value of this holding using yahoofinance webreader --> do for each ticker
#   

import mysql.connector
import pandas as pd
import pandas_datareader.data as web
import datetime as dt 

# First, make a connection to the SQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="SammySQL@7s",
    database = "stockdatabase"
)

# Make the cursor based on the established connection
cursor = connection.cursor()

# Make the table to hold user ID's ------------------------

# cursor.execute("""
# CREATE TABLE users (
#     user_id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255)
# )
# """)

# Make the table to hold the user's portfolio --> use normalization on user_id --------------------------

# cursor.execute("""
# CREATE TABLE portfolios (
#     id INT,
#     ticker VARCHAR(4),
#     date_purchased DATE,
#     number_shares INT,
#     purchase_price DECIMAL(15,2),

#     FOREIGN KEY(id) REFERENCES users(user_id)
# )
# """)

# Populate Tables - do this in SQL!

# **Given the ID, show the portfolio for this person (stock:number of shares)**:

# take in input, store the id in a variable
# for loop through all of the rows of the sql table that contains portfolio entries
# if the id matches with the id column, make dictionary for {TICKER: NUMBER OF SHARES}
#   Two cases:
#       if ticker already exists, need to sum the shares
#       if the ticker does not exist, make a new entry in the list and make new dictionary entry

# Read the sql table into a pandas dataframe

users_sql = pd.read_sql_query("SELECT * FROM users", connection)
print(users_sql)
portfolios_sql = pd.read_sql_query("SELECT * FROM portfolios", connection)
print(portfolios_sql)

# print(portfolios_sql.columns)

# get the user that we want to look at
id_input = input("Enter the user ID: ")
print(type(id_input))

# List to show holdings for the user_id
holdings_shares = {}

# iterate through all of the rows
for i, row in portfolios_sql.iterrows():
    # if there is a match with the ID we are looking for
    if portfolios_sql['id'][i] == int(id_input):
        # If it is already present, we need to be able to simply add the shares together
        if portfolios_sql['ticker'][i] in holdings_shares:
            holdings_shares[portfolios_sql['ticker'][i]] += portfolios_sql['number_shares'][i]
        # else, we can add a new entry to the list
        else:
            holdings_shares[portfolios_sql['ticker'][i]] = portfolios_sql['number_shares'][i]
        
# Now that we have a dictionary with all of the holdings of a person, we can try and display some metrics based on this
# First, let's see how much money is in each company --> show {'ticker': $ amount}

# get df from yahoo finance
startdate = dt.datetime(2021,8,1)
enddate = dt.datetime.today()

# make lists to access the symbols and # shares from dictionary
ticker_symbols = list(holdings_shares.keys())
ticker_shares = list(holdings_shares.values())

# print(ticker_symbols)
# print(ticker_shares)

# dictionary to hold {'ticker': $ amount}
holdings_amounts = {}

# loop through the ticker symbols
for i in range(len(ticker_symbols)):
    # make a pandas dateframe for data from yahoo finance based on the ticker symbol we're looking at
    df = web.DataReader(ticker_symbols[i], 'yahoo', startdate, enddate)
    # print(df)
    # add to the dictionary
    holdings_amounts[ticker_symbols[i]] = ticker_shares[i] * df['Close'][-1]

print(holdings_shares)
print(holdings_amounts)



