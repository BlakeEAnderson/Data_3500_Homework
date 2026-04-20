import json
import requests
import datetime
import time
import csv

# after getting the csv files

# 5 day moving average
# list of urlcoins
urlcoins = ["ethereum", "bitcoin", "tether", "chainlink", "tron", "usds"]

# for every coin
for i in urlcoins:

    # open and put each line into lines variable
    file = open( str(i) + ".csv")
    lines = file.readlines()
    reader = csv.reader(lines)
    # variables buy, sell, overall, priceLst
    
    buy = 0
    sell = 0
    overall = 0
    priceLst = []

    # fill price list with prices
    for row in reader:
        price = float(row[1]) # sets it as a float
        price = round(price, 2) # rounds price
        priceLst.append(price) # appends to list

    # itterates through price list and displays the moving average
    print(i)    
    for i in range(len(priceLst)):
        # calc 5 day avg
        # makes sure its not out of range
        if i <= 5:
            # creates current price and the average for the day
            currentPrice = priceLst[i]
            average = (priceLst[i] + priceLst[i+1] + priceLst[i+2] + priceLst[i+3] + priceLst[i+4])/5
        else:
            break

        # check if below 98% of 5 day average
        if currentPrice < average * .98:
            #buy
            buy = currentPrice
            print(f"Buying at: {buy}")

        elif currentPrice > average * 1.02:
            # sell
            sell = currentPrice
            tradeValue = buy - sell
            print(f"Selling at: {sell} Profit:{round(tradeValue, 2)}")
            overall = overall + tradeValue
        else:
            # do nothing
            overall += 0
    print(f"TOTAL PROFIT: {round(overall,2)}")    