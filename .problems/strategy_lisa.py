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
    # 5 - Challenge Problem
    # Lisa's circumstances:
    # - She purchased $12,000 worth of stock in the beginning of 2020, BUT:
    # - if the stock drops BELOW 8% from previous day's close, she sells half of her stock
    # - she will then RE-INVEST if the stock recovers to when she had sold it
    # How much is his investment worth at the end of 2020?
    #-----------------------------------

    #Lisa Starting Amount        
    LisaPortfolio = 12000

    soldprices = []
    soldamounts = []

    #variables that describe the price we sold the stock at, how much we sold, and a tester variable
    sellStockPrice = 0
    sellAmt = 0

    #loop through the entire dataframe
    for i in range(1, len(openCol)-1):
        
        #update value of portfolio each time a market day elapses
        LisaPortfolio += LisaPortfolio * (openCol[i] - closeCol[i-1])/closeCol[i-1]
        #print(LisaPortfolio)

        #if stock drops 8% or more in a day...
        if((openCol[i] - closeCol[i-1]) / closeCol[i-1] <= -0.08):
            #keep track of the price we sold the stock at
            soldprices.append(openCol[i])
            #keep track of the amount of our portfolio we sold (half)
            soldamounts.append(LisaPortfolio / 2)
            #update lisa's portfolio by subtracting the amount we sold (the half amount)
            LisaPortfolio -= LisaPortfolio / 2
            #print("SELL ", LisaPortfolio, df["Date"][i])
            
        for amount, price in zip(soldamounts, soldprices):
            if (closeCol[i] >= price):
                LisaPortfolio += amount
                #print("BUY ", amount, df["Date"][i])
                soldamounts.pop()
                soldprices.pop()

    print("Lisa's initial investment grew to ${:,.2f}".format(LisaPortfolio))

if __name__ == "__main__":
    main()