# https://api.coingecko.com/api/v3/coins/ethereum/history?date=25-11-2025&localization=false

import json
import requests
import datetime
import time
import csv

# url setup
url1 = "https://pro-api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
headers = {"x-cg-pro-api-key": "CG-RPB9RntnigsxQbwRtavehcv9"}

#https://pro-api.coingecko.com/api/v3/ping?x_cg_pro_api_key=YOUR_API_KEY
# coin
urlcoins = ["bitcoin", "tether", "chainlink", "tron", "usds"] #,"ethereum"

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

        print(url)

        # make dictionary
        eth_dictionary = json.loads(request.text)
        try:
            print(eth_dictionary[marketKey][priceKey][usdKey])
            fileLines.append(dateFormat + ", " + str(eth_dictionary[marketKey][priceKey][usdKey]) + "\n")
        except:
            print("NO MORE CALLS")
    # write to a file
    file.writelines(fileLines)


