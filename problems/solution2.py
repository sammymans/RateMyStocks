from os import close
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
    #df.to_csv('tesla.csv')

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
    # 2
    # Jason invested $12,000 worth of TSLA at the beginning of 2020.
    # How much is his investment worth at the end of 2020?
    #-----------------------------------

    initialJ = 12000

    openCol = df["Open"]
    openPrice = openCol[0]

    closeCol = df["Adj Close"]
    closePrice = closeCol[len(closeCol)-1]

    gain = closePrice - openPrice
    percentGain = gain / openPrice

    #print(gain, percentGain)

    newAmt = initialJ * percentGain

    print("Jason's initial investment grew to ${:,.2f}".format(newAmt))

    #-----------------------------------
    # 3
    # Tammy's circumstance:
    # - She has $12,000 worth of money to be invested
    # - Only invests $1,000 if and only if the stock drops 5% from previous day
    # How much is her investment worth at the end of 2020?
    #-----------------------------------

    savingsTammy = 12000
    updateSavings = 0

    invAmt = 1000
    tslaValue = []
    resultTammy = 0

    lastDayVal = closeCol[len(closeCol)-1]

    # Recall openCol and closeCol from #2

    for i in range(1,len(openCol)):

        if((openCol[i] - closeCol[i-1])/closeCol[i-1] <= -0.05):

            tslaValue.append(openCol[i])

            savingsTammy = savingsTammy - invAmt
            updateSavings += invAmt
            if(savingsTammy == 0):
                break

    for val in tslaValue:
        resultTammy += (lastDayVal - val)*1000/val

    resultTammy += updateSavings
    
    print("Tammy's initial investment grew to ${:,.2f}".format(resultTammy))

    
    





if __name__ == "__main__":
    main()