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
    # 3
    # Tammy's circumstances:
    # - She has $12,000 worth of money to be invested
    # - Only invests $1,000 if and only if the stock drops 5% from previous day
    # How much is her investment worth at the end of 2020?
    #-----------------------------------

    #Tammy's initial savings
    savingsTammy = 12000
    #Number to be updated later
    updateSavings = 0

    #The amount Tammy will invest each time
    invAmt = 1000
    #array to hold the values for the times Tammy invested in TSLA stock
    tslaValue = []

    #Total amount she has at the end of 2020
    resultTammy = 0

    #how much TSLA stock is worth on the last day of 2020
    lastDayVal = closeCol[len(closeCol)-1]

    #loop through, starting from the second day --> need to be able to look at the day before in order to calculate a percent diff
    for i in range(1,len(openCol)):
        #if the percent gain is less than or equal to -5%
        if((openCol[i] - closeCol[i-1])/closeCol[i-1] <= -0.05):
            #add the value of the TSLA at that moment to our array
            tslaValue.append(openCol[i])

            #reduce how much Tammy has in her savings
            savingsTammy = savingsTammy - invAmt
            #add to variable how much has been invested so far
            updateSavings += invAmt
            #if her savings amount reaches 0, break from the loop
            if(savingsTammy == 0):
                break

    #calculate how much each seperate investment has grown and add to the total
    for val in tslaValue:
        resultTammy += (lastDayVal - val)*invAmt/val

    #add how much Tammy has invested to reflect proper amount in her account
    resultTammy += updateSavings
    print("Tammy's initial investment grew to ${:,.2f}".format(resultTammy))

if __name__ == "__main__":
    main()