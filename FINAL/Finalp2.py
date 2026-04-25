"""
This is part 2 of my final project which simulates trading strategies for each csv file
which hold the dates and the value of the coins at those dates. Then writes thos to
a json file and outputs into seperate json files.
"""


import json
import requests
import datetime
import time
import csv

def csvtojson(csvFileName, jsonFileName):
    # open csvFile
    with open(csvFileName, 'r') as csvFile:
        # write the data to a variable
        data = list(csv.DictReader(csvFile))

    # open new json file
    with open(jsonFileName, "w") as jsonFile:
        # write 5day dataset to the file
        json.dump(data, jsonFile, indent = 4)
    
def highestCalc(fileName):
    file = open(fileName)
    lines = file.readlines()
    reader = csv.reader(lines)
    high = 0
    name = ""
    for row in reader:
        # this is used to bypass the first line which will be a string
        try:
            amount = float(row[3])
            # check if its a new high
            if amount > high:
                high = amount
                name = row[0]
            else:
                high += 0
        except:
            high += 0
    returnString = f"THE HIGHEST GROSS FOR 5 DAY WAS: {name}: \t PERCENT GAIN: {high}"
    return(returnString)
# run after getting the csv files

# list of urlcoins
# change usds, tether,
urlcoins = ["bitcoin", "solana", "chainlink", "tron", "whitebit", "ethereum"]

# counter variable
x = 0

# start of 5 day average loop
# for every coin
# create a top line for file
fileLines = ["Name, First Buy, Total Profit, Percent Gain, Price High, Price High Date, Price Low, Price Low Date\n"]
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
            print(f"SELLING AT: \t{currentPrice} \t PROFIT:\t{round(tradeValue, 2)}")
            
            
            
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

    # write to the dictionary with the data
    #format: Name, First Buy, Total Profit, Percent Gain, Price High, Price Low
    fileLines.append(str(name) + ", " + str(firstBuy) + ", " + str(totalProfit) + "," + str(((totalProfit - firstBuy)/firstBuy) * 100) + ", " + str(priceHigh) + ", " + str(priceHighDate) + ", " + str(priceLow) + ", " + str(priceLowDate) + "\n")
    
    # add to the counter var
    x += 1
# open a dictionary
file = open("5DayAverage.csv", "w")
file.writelines(fileLines)

# resets fileLines
fileLines = ["Name, First Buy, Total Profit, Percent Gain, Price High, Price High Date, Price Low, Price Low Date\n"]

# start of 10 day average
for t in urlcoins:
    # open and put each line into lines variable
    file = open( str(t) + ".csv")
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
    print(t)
    name = str(t)

    for t in range(len(priceLst)):
        if t <= 355:
        # creates current price and the average for the day
            currentPrice = priceLst[t]
            # creates a 10 day moving average
            average = (priceLst[t] + priceLst[t+1] + priceLst[t+2] + priceLst[t+3] + priceLst[t+4] + priceLst[t+5] + priceLst[t+6] + priceLst[t+7] + priceLst[t+8] + priceLst[t+9])/10

        else:
            break

        # check if its the first purchace and change the value if it is and nothing if not
        if firstBuy == 0:
            firstBuy = currentPrice
            priceHigh = currentPrice
            priceHighDate = dateLst[t]
            priceLow = currentPrice
            priceLowDate = dateLst[t]

        # check if its a new high
        if currentPrice > priceHigh:
            priceHigh = currentPrice
            priceHighDate = dateLst[t]

        # check and update priceLow
        if currentPrice < priceLow:
            priceLow = currentPrice
            priceLowDate = dateLst[t]
    
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
            print(f"SELLING AT: \t{currentPrice} \t PROFIT:\t{round(tradeValue, 2)}")
            
            
            
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

    # write to the dictionary with the data
    #format: First Buy, Total Profit, Percent Gain, Price High, Price Low
    fileLines.append(name + ", " + str(firstBuy) + ", " + str(totalProfit) + "," + str(((totalProfit - firstBuy)/firstBuy) * 100) + ", " + str(priceHigh) + ", " + str(priceHighDate) + ", " + str(priceLow) + ", " + str(priceLowDate) + "\n")
       
    # add to the counter var
    x += 1
# open a dictionary

        # I USED AI FOR THESE NEXT TWO LINES TO FIX AN ERROR #
"""
what the AI said
        # Replace this:
            file = open("10DayAverage.csv", "w")
            file.writelines(fileLines)

        # With this:
            with open("10DayAverage.csv", "w") as file:
                file.writelines(fileLines)
"""



# saves both files to a json
csvtojson("5DayAverage.csv", "5DayResults.json")
csvtojson("10DayAverage.csv", "10DayResults.json")

print(highestCalc("5DayAverage.csv"))
print(highestCalc("10DayAverage.csv"))