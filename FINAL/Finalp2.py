"""
This is part 2 of my final project which simulates trading strategies for each csv file
which hold the dates and the value of the coins at those dates.
"""


import json
import requests
import datetime
import time
import csv

# run after getting the csv files

# list of urlcoins
urlcoins = ["ethereum", "bitcoin", "tether", "chainlink", "tron", "usds"]
# counter variable
x = 0

# for every coin
for i in urlcoins:

    # open and put each line into lines variable
    file = open( str(i) + ".csv")
    lines = file.readlines()
    reader = csv.reader(lines)

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
    for j in range(len(priceLst)):
        # makes sure its not out of range
        if j <= 360:
            # creates current price and the average for the day
            currentPrice = priceLst[j]
            # creates a 5 day moving average
            average = (priceLst[j] + priceLst[j+1] + priceLst[j+2] + priceLst[j+3] + priceLst[j+4])/5

        else:
            break

        # check if its the first purchace and change the value if it is and nothing if not
        if firstBuy == 0:
            firstBuy = currentPrice
            priceHigh = currentPrice
            priceHighDate = dateLst[j]
            priceLow = currentPrice
            priceLowDate = dateLst[j]

        # check if its a new high
        if currentPrice > priceHigh:
            priceHigh = currentPrice
            priceHighDate = dateLst[j]

        # check and update priceLow
        if currentPrice < priceLow:
            priceLow = currentPrice
            priceLowDate = dateLst[j]
    
        if currentPrice > average and buy == 0:
            #buy
            buy = currentPrice
            print(f"BUYING AT: {buy}")

        elif currentPrice < average and buy != 0:
            # sell
            tradeValue = currentPrice - buy
            print(f"SELLING AT: {currentPrice} \t PROFIT:{round(tradeValue, 2)} \t AVERAGE:{average}")
            overall += tradeValue
            
            # reset buy value
            buy = 0
    # checks the final day and gives a suggestion            
    if currentPrice > average:
        suggestion = "You should buy on the last day"
    elif currentPrice < average:
        suggestion = "You should sell on the last day"
    else:
        suggestion = "Just hold your current price"
    
    # output for each coin
    print("\n\n___________________________")
    print(f"FIRST BUY: {round(firstBuy, 2)}")
    print(f"TOTAL PROFIT: {round(overall,2)}")
    print(f"PERCENT GAIN: {round((overall/firstBuy) * 100,2)}")
    print(f"PRICE HIGH: {round(priceHigh, 2)} ON DATE: {priceHighDate}")
    print(f"PRICE LOW: {round(priceLow, 2)} ON DATE: {priceLowDate}")
    print(suggestion)
    print("___________________________\n\n")

    # create a dictionary
    file = open(str(urlcoins[x]) + " data.csv", "w")
    fileLines = []

    # write to the dictionary with the data
    #format: First Buy, Total Profit, Percent Gain, Price High, Price Low
    fileLines.append(str(firstBuy) + ", " + str(overall) + "," + str((overall/firstBuy) * 100) + ", " + str(priceHigh) + ", " + str(priceHighDate) + ", " + str(priceLow) + ", " + str(priceLowDate))
    file.writelines(fileLines)
    
    # add to the counter var
    x += 1
    