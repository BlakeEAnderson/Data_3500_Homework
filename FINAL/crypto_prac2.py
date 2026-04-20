import json
import requests
import datetime
import time
import csv

# after getting the csv files

# 5 day moving average
# list of urlcoins
urlcoins = ["ethereum"] #, "bitcoin", "tether", "chainlink", "tron", "usds"]

# for every coin
for i in urlcoins:

    # open and put each line into lines variable
    file = open( str(i) + ".csv")
    lines = file.readlines()
    reader = csv.reader(lines)

    # buylock
    buyLock = 0

    # variables buy, sell, overall, priceLst
    firstBuy = 0
    buy = 0
    sell = 0
    overall = 0
    priceLst = []
    dateLst = []

    # high and low variables
    priceHigh = 0
    priceLow = 0
    priceHighDate = ""
    priceLowDate = ""

    # final suggestion
    suggestion = ""
    # fill price list with prices
    for row in reader:
        price = float(row[1]) # sets it as a float
        date = row[0] # sets the date for each price
        price = round(price, 2) # rounds price
        priceLst.append(price) # appends to list
        dateLst.append(date) # appends date

    # itterates through price list and displays the moving average
    print(i)    
    for i in range(len(priceLst)):
        # makes sure its not out of range
        if i <= 44:
            # creates current price and the average for the day
            currentPrice = priceLst[i]
            # creates a 5 day moving average
            average = (priceLst[i] + priceLst[i+1] + priceLst[i+2] + priceLst[i+3] + priceLst[i+4])/5
        else:
            break
        # check if its the first purchace and change the value if it is and nothing if not
        if firstBuy == 0:
            firstBuy = currentPrice
            priceLow = currentPrice
            priceHigh = currentPrice
        else:
            firstBuy += 0 

        # check if its a new high
        if currentPrice > priceHigh:
            priceHigh = currentPrice
            priceHighDate = dateLst[i]
        else:
            priceHigh += 0
        # check and update priceLow
        if currentPrice < priceLow:
            priceLow = currentPrice
            priceLowDate = dateLst[i]
        else:
            priceLow += 0

        # check if below 98% of 5 day average
        if buyLock == 0:
            if currentPrice < average * .98:
                #buy
                buy = currentPrice
                print(f"BUYING AT: {buy}")
                buyLock = 1
        elif buyLock == 1:
            # check if above 2% of 5 day average
            if currentPrice > average * 1.02:
                # sell
                sell = currentPrice
                tradeValue = sell - buy
                print(f"SELLING AT: {sell} \t PROFIT:{round(tradeValue, 2)}")
                overall = overall + tradeValue
                buyLock = 0
            else:
                # do nothing
                overall += 0

    # checks the final day and gives a suggestion            
    if currentPrice > average*98:
        suggestion = "You should buy on the last day"
    elif currentPrice < average*1.02:
        suggestion = "You should sell on the last day"
    
    # output for each coin
    print("\n\n___________________________")
    print(f"FIRST BUY: {round(firstBuy, 2)}")
    print(f"TOTAL PROFIT: {round(overall,2)}")
    print(f"PERCENT GAIN: {round((firstBuy/overall),2)}")
    print(f"PRICE HIGH: {round(priceHigh, 2)} ON DATE: {priceHighDate}")
    print(f"PRICE LOW: {round(priceLow, 2)} ON DATE: {priceLowDate}")
    print(suggestion)
    print("___________________________\n\n")   