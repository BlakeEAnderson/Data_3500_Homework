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
urlcoins = ["chainlink"]#, "bitcoin", "tether", "chainlink", "tron", "usds"]

# counter variable
x = 0

# for every coin
for i in urlcoins:

    # open and put each line into lines variable
    file = open( str(i) + ".csv")
    lines = file.readlines()
    reader = csv.reader(lines)

    # variables buy, sell, totalProfit, priceLst
    firstBuy = 0
    buy = 0
    sell = 0
    totalProfit = 0
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
    name = i    
    for i in range(len(priceLst)):
        # makes sure its not out of range
        if i <= 360:
            # creates current price and the average for the day
            currentPrice = priceLst[i]
            # creates a 5 day moving average
            average = (priceLst[i] + priceLst[i+1] + priceLst[i+2] + priceLst[i+3] + priceLst[i+4])/5

        else:
            break

        # check if its the first purchace and change the value if it is and nothing if not
        if firstBuy == 0:
            firstBuy = currentPrice
            priceHigh = currentPrice
            priceHighDate = dateLst[i]
            priceLow = currentPrice
            priceLowDate = dateLst[i]

        # check if its a new high
        if currentPrice > priceHigh:
            priceHigh = currentPrice
            priceHighDate = dateLst[i]

        # check and update priceLow
        if currentPrice < priceLow:
            priceLow = currentPrice
            priceLowDate = dateLst[i]
    
        if currentPrice < (average * 0.98) and buy == 0:
            #buy
            buy = currentPrice
            print(f"BUYING AT: \t{buy}")

        elif currentPrice > (average * 1.02) and buy != 0:
            # sell
            tradeValue = currentPrice - buy

            # reset buy value
            buy = 0
            
            totalProfit += tradeValue
            print(f"SELLING AT: \t{currentPrice} \n PROFIT:\t{round(tradeValue, 2)}")
            
            
            
    # checks the final day and gives a suggestion            
    if currentPrice > average:
        suggestion = "You should buy on the last day"
    elif currentPrice < average:
        suggestion = "You should sell on the last day"
    else:
        suggestion = "Just hold your current price"
    
    # output for each coin
    print("\n\n___________________________________________________________")
    print(name.upper() + "\n")
    print(f"FIRST BUY: \t{round(firstBuy, 2)}")
    print(f"TOTAL PROFIT: \t{round(totalProfit,2)}")
    print(f"PERCENT RETURN: \t{round( (totalProfit/firstBuy) * 100 ,2)}")
    print(f"PRICE HIGH: \t{round(priceHigh, 2)} ON DATE: {priceHighDate}")
    print(f"PRICE LOW: \t{round(priceLow, 2)} ON DATE: {priceLowDate}")
    print(suggestion)
    print("___________________________________________________________\n\n")

    # create a dictionary
    file = open(str(urlcoins[x]) + " data.csv", "w")
    fileLines = []

    # write to the dictionary with the data
    #format: First Buy, Total Profit, Percent Gain, Price High, Price Low
    fileLines.append(str(firstBuy) + ", " + str(totalProfit) + "," + str(((totalProfit - firstBuy)/firstBuy) * 100) + ", " + str(priceHigh) + ", " + str(priceHighDate) + ", " + str(priceLow) + ", " + str(priceLowDate))
    file.writelines(fileLines)
    
    # add to the counter var
    x += 1
    