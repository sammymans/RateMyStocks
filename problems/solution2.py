import pandas as pd
import pandas_datareader.data as web
import datetime as dt

def main():
    startdate = dt.datetime(2020,1,1)
    enddate = dt.datetime(2021,1,1)

    #result = web.DataReader('TSLA', 'yahoo', startdate, enddate)

    # Save to CSV
    #result.to_csv('tesla.csv')

    # Read from CSV
    #result = pd.read_csv('tesla.csv')
    #print(result)

if __name__ == "__main__":
    main()