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


# PROBLEM 2:
# Given two arrays, write a function that returns the overall dollar($) and percent(%) gain/loss
# The first array contains the current market price of equities
# The second array contains the original purchase price of equities
# Ex.
# currentValue = [ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24], ['MSFT', 250, 6], ['SQ', 274, 5], ['GME', 275, 23] ]
# purchaseValue = [ ['AAPL', 98], ['TSLA', 245], ['MSFT', 341], ['SQ', 255], ['GME', 275] ]

#Note, gain is equal to (current-purchase) for $ and (current-purchase)/purchase for %

def gain(currentValue, purchaseValue):    
    totalworth = 0
    originalworth = 0

    for currentstock, purchasedstock in zip(currentValue, purchaseValue):
        originalworth += purchasedstock[1] * currentstock[2]
        totalworth += currentstock[1] * currentstock[2]

    return (totalworth - originalworth), ((totalworth - originalworth)*100/originalworth)

def main():
    print(portfolioWorth([ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24], ['MSFT', 250, 6], ['SQ', 274, 5], ['GME', 275, 23] ]))
    
    currentValue = [ ['AAPL', 160.23, 10], ['TSLA', 680.34, 24], ['MSFT', 250, 6], ['SQ', 274, 5], ['GME', 275, 23] ]
    purchaseValue = [ ['AAPL', 98], ['TSLA', 245], ['MSFT', 341], ['SQ', 255], ['GME', 275] ]
    print(gain(currentValue, purchaseValue))

if __name__ == "__main__":
    main()
