"""
This is part one of my final project for DATA 3500. This part of the code takes the urls
from coingecko and takes the dictionary that is recived and records the value of the
coin and the date the value was gotten. These are recorded into csv files labeled after
the coin that they were gotten from. example - bitcoin.csv
"""
import json
import requests
import datetime
import time
import csv

# url setup
url1 = "https://pro-api.coingecko.com/api/v3/coins/"
url2 = "/history?date="

# header variable to hold my api key
headers = {"x-cg-pro-api-key": "CG-RPB9RntnigsxQbwRtavehcv9"}


# coin
urlcoins = ["bitcoin", "tether", "chainlink", "tron", "usds","ethereum"]

# date
today = datetime.datetime.now()

# url keys
marketKey = "market_data"
priceKey = "current_price"
usdKey = "usd"

for coin in urlcoins:
    file = open(coin+".csv", "w")
    fileLines = []
    # set startdate
    startdate = today - datetime.timedelta(days=366)
    print(startdate)

    # create heading for csv file
    for i in range(365):
        #time
        time.sleep(1)
        # add one to the start date each loop & format it
        startdate += datetime.timedelta(days=1)
        dateFormat = startdate.strftime("%Y-%m-%d")

        # make a full url
        url = url1 + coin + url2 + str(dateFormat)

        request = requests.get(url, headers=headers)

        # print(url) # used to catch bugs with the url

        # make dictionary
        eth_dictionary = json.loads(request.text)

        # print the value of the coin and append it and the date to a csv
        try:
            print(eth_dictionary[marketKey][priceKey][usdKey])
            fileLines.append(dateFormat + ", " + str(eth_dictionary[marketKey][priceKey][usdKey]) + "\n")
        
        # exception for if any problem is detected while appeneding or getting the data
        except:
            # error msg
            print("NO MORE CALLS")

    # write to a file
    file.writelines(fileLines)
    