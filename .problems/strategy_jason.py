from os import close
import pandas as pd
import pandas_datareader.data as web
import datetime as dt

def main():
    #-----------------------------------
    #1 - Get basic stock pricing on day-to-day basis
    #-----------------------------------
    
    startdate = dt.datetime(2021,1,1)
    enddate = dt.datetime(2021,7,1)

    df = web.DataReader('VIPS', 'yahoo', startdate, enddate)
    df.reset_index(inplace=True,drop=False)
    df['Date'] 


    # Print first couple data entries to make sure data is correct
    print(df.head())

    # 1a - Save to CSV
    #df.to_csv('tesla.csv', )

    # Read from CSV
    #df = pd.read_csv('tesla.csv')
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
    # 2
    # Jason invested $12,000 worth of TSLA at the beginning of 2020.
    # How much is his investment worth at the end of 2020?
    #-----------------------------------

    #Jason's initial investment
    initialJ = 12000

    #variables to store date from the column "open"
    openCol = df["Open"]
    #variable to get the opening price for 2020
    openPrice = openCol[0]

    #variable to store data from the column "adj close"
    closeCol = df["Adj Close"]
    #variable to get the final closing price for 2020
    closePrice = closeCol[len(closeCol)-1]

    #calculate the gain, then the percent gain over the year 2020
    gain = closePrice - openPrice
    percentGain = gain / openPrice

    #print(gain, percentGain)

    #calculate and print how much Jason has in his account
    newAmt = initialJ * (1.0 + percentGain)
    print("Jason's initial investment grew to ${:,.2f}".format(newAmt))

if __name__ == "__main__":
    main()