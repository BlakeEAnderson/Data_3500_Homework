# https://api.coingecko.com/api/v3/coins/ethereum/history?date=25-11-2025&localization=false

import json
import requests
import datetime
import time
# url setup
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

# coin
urlcoins = ["ethereum", "bitcoin"]

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
    for i in range(4):
        #time
        time.sleep(11)
        # add one to the start date each loop & format it
        startdate += datetime.timedelta(days=1)
        dateFormat = startdate.strftime("%d-%m-%Y")

        # make a full url
        url = url1 + coin + url2 + str(dateFormat) + url3
        request = requests.get(url)

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