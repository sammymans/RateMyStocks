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
    newAmt = initialJ * percentGain
    print("Jason's initial investment grew to ${:,.2f}".format(newAmt))

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
    newMonth = 1
    
    #loop through the entire length of the dataframe
    for i in range(len(openCol-1)):
        #split the data string in order to access just the month component
        splitString = dateCol[i].split("-")
        month = splitString[1]

        #if the month changes, add the value to the array
        if(month != newMonth):
            investments.append(openCol[i])

        #update
        newMonth = month

    #calculate how much each seperate investment has grown and add to the total
    for val in investments:
        resultJohnny += (lastDayVal - val)*invAmount/val

    #add how much Tammy has invested to reflect proper amount in her account
    resultJohnny += savingsJohnny
    print("Johnny's initial investment grew to ${:,.2f}".format(resultJohnny))
    
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

    #variables that describe the price we sold the stock at, how much we sold, and a tester variable
    sellStockPrice = 0
    sellAmt = 0
    j = 0

    #loop through the entire dataframe
    for i in range(1, len(openCol)-1):
        
        #update value of portfolio each time a market day elapses
        LisaPortfolio += LisaPortfolio * (openCol[i] - closeCol[i-1])/closeCol[i-1]
        print(LisaPortfolio)

        #if stock drops 8% or more in a day...
        if((openCol[i] - closeCol[i-1]) / closeCol[i-1] <= -0.08):
                #keep track of the price we sold the stock at
                sellStockPrice = openCol[i]
                #keep track of the amount of our portfolio we sold (half)
                sellAmt = LisaPortfolio / 2
                #update lisa's portfolio by subtracting the amount we sold (the half amount)
                LisaPortfolio = LisaPortfolio - sellAmt
                #make a count for when the stock drops 8%
                j+=1


        #if stock returns to previous price, buy back amount previously sold 
        if((openCol[i] >= sellStockPrice) and j ==1):
            #add back the amount we sold to our portfolio so it can earn interest again
            LisaPortfolio += sellAmt
            #reset j to zero
            j = 0

    print("Lisa's initial investment grew to ${:,.2f}".format(LisaPortfolio))
    
    #THE PROBLEM WITH THE CODE FOR QUESTION 5:
    # This code only works because there are no two consecutive days where the stock can drop by 8%
    # The issue with the code and why it does not solve the problem mentioned is because I don't have a way to track
    # more than one drop, and then a way to also track when the stock recovers back to these multiple values
    #
    # need to think of a way to solve the consecutive 8% drop days


if __name__ == "__main__":
    main()