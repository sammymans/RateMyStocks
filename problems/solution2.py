import pandas as pd
import pandas_datareader.data as web
import datetime as dt

def main():
    #-----------------------------------
    #1 - Get basic stock pricing on day-to-day basis
    #-----------------------------------
    
    startdate = dt.datetime(2020,1,1)
    enddate = dt.datetime(2021,1,1)

    df = web.DataReader('TSLA', 'yahoo', startdate, enddate)

    # Print first couple data entries to make sure data is correct
    print(df.head())

    # 1a - Save to CSV
    df.to_csv('tesla.csv')

    # Read from CSV
    df = pd.read_csv('tesla.csv')
    print(df)

    # 1b - Find Average
    
    #Print average for 'High' column
    print(df["High"].mean())
    #Print average for 'Low' column using dot notation
    print(df.Low.mean())
    #Print mean of multiple columns
    print(df[["Open", "Close"]].mean())
    #General description of dataframe
    print(df.describe())

    #-----------------------------------
    #2
    # Jason invested $12,000 worth of TSLA at the beginning of 2020.
    # How much is his investment worth now?
    #-----------------------------------

    initial = 12000

    openCol = df["Open"]
    openPrice = openCol[0]

    closeCol = df["Close"]
    closePrice = closeCol[len(closeCol)-1]

    gain = closePrice - openPrice
    percentGain = gain / openPrice

    print(gain, percentGain)

    newAmt = initial * percentGain

    print(newAmt)

if __name__ == "__main__":
    main()