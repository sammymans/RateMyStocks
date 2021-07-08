# PROBLEM 1:
# Write a function that returns the overall portfolio worth (as type float) provided:
# ticker symbol, stock price, and number of shares
# Ex.
# holdings = [ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24] ]

def portfolioWorth(holdings):
    totalWorth = 0

    for i in range(len(holdings)):
        totalWorth += holdings[i][1] * holdings[i][2]

    print("Value of total portfolio is:\n${:,}".format(totalWorth))

    stockWorth = {company[0]: company[1]*company[2] for company in holdings}
    print("\nValue of individual company's are: ")
   
    return stockWorth

print(portfolioWorth([ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24], ['MSFT', 250, 6], ['SQ', 274, 5], ['GME', 275, 23] ]))
print("\n\n")

# PROBLEM 2:
# Given two arrays, write a function that returns the overall dollar($) and percent(%) gain/loss
# The first array contains the current market price of equities
# The second array contains the original purchase price of equities
# Ex.
# currentValue = [ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24], ['MSFT', 250, 6], ['SQ', 274, 5], ['GME', 275, 23] ]
# purchaseValue = [ ['AAPL', 98], ['TSLA', 245], ['MSFT', 341], ['SQ', 255], ['GME', 275] ]

#Note, gain is equal to (current-purchase) for $ and (current-purchase)/purchase for %

def gain(currentValue, purchaseValue):
    
    curValStocks = []
    purValStocks = []
    overallGain = []
    percentGain = []

    for i in range(len(purchaseValue)):
        purValStocks.append(purchaseValue[i][1])
        curValStocks.append(currentValue[i][1])
        overallGain.append((curValStocks[i] - purValStocks[i]))
        percentGain.append(overallGain[i]/purValStocks[i])

    portfolioPurVal = 0
    totalWorth = 0

    for i in range(len(currentValue)):
        totalWorth += currentValue[i][1] * currentValue[i][2]

    for i in range(len(purchaseValue)):
        portfolioPurVal += purValStocks[i]*currentValue[i][2]

    print("Value of original portfolio is:\n${:,}".format(portfolioPurVal))
    print("Overall gain on portfolio is:\n${:,}".format(totalWorth - portfolioPurVal))
    print("Overall percent gain on portfolio is:\n{:.2f}%".format((totalWorth - portfolioPurVal)*100/portfolioPurVal))
    print("\n")

    return overallGain, percentGain

currentValue = [ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24], ['MSFT', 250, 6], ['SQ', 274, 5], ['GME', 275, 23] ]
purchaseValue = [ ['AAPL', 98], ['TSLA', 245], ['MSFT', 341], ['SQ', 255], ['GME', 275] ]
print(gain(currentValue, purchaseValue))