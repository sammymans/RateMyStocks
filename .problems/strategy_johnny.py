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
    # 4
    # Johnny's circumstances:
    # - He invests $1,000 at the start of each month, regardless of price (i.e., Dollar Cost Average (DCA))
    # How much is his investment worth at the end of 2020?
    #-----------------------------------

    #variable to hold data from the date column
    dateCol = df["Date"]

    #variables for Johnny's savings, how much he invests each time, and his total return
    savingsJohnny = 12000
    invAmount = 1000
    resultJohnny = 0

    #array to hold the value of TSLA stock each time he trades
    investments = []

    #dynamic variable to see if the month has changed
    month_hold = 0

    #loop through the entire length of the dataframe
    for i in range(len(openCol-1)):
        if (dateCol[i].month != month_hold):
            investments.append(openCol[i])
            month_hold = dateCol[i].month

    #calculate how much each seperate investment has grown and add to the total
    for val in investments:
        resultJohnny += (lastDayVal - val)*invAmount/val

    #add how much Tammy has invested to reflect proper amount in her account
    resultJohnny += savingsJohnny
    print("Johnny's initial investment grew to ${:,.2f}".format(resultJohnny))
    
    
if __name__ == "__main__":
    main()