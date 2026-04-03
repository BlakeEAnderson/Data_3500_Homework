def simpleMovingAvg(openfile):

    # link file
    file = open(openfile)
    lines = file.readlines()

    # set values of buy, sell, overall_value
    buy = 0
    sell = 0
    overall_value = 0
    
    # list to hold the prices
    price_lst = []
    for line in lines:
        price = float(line)
        price = round(price, 2) # to round the price to 2 decimals
        price_lst.append(price)

    # iterate through the list
    for i in range(len(price_lst)):
        # checks to make sure the average wont be out of range
        if i <= 246:
            # calculate current price
            current_price = price_lst[i]
            # calculate 5 day moving avg
            moving_avg = (price_lst[i] + price_lst[i+1] + price_lst[i+2] + price_lst[i+3] + price_lst[i+4])/5
        else:
            break
        # if statement to check if current price is below 5 day avg
        if current_price < moving_avg*.98:
            # buy stock
            # check if it is first purchase
            if buy == 0:
                first_buy = current_price
                buy = current_price
                print(f"Buying at:      {buy}")
            else:
                buy = current_price
                print(f"Buying at:      {buy}")
        elif current_price > moving_avg*1.02:
            # sell stock
            sell = current_price
            print(f"Selling at:     {sell}")

            # calculate the amount earned and add it to the total
            trade_value = sell - buy
            print(f"Trade Value:        {round(trade_value,2)}")
            overall_value += trade_value
        else:
            # dont buy or sell
            overall_value += 0
    final_profit_percentage = (overall_value / first_buy) * 100
    print("----------------------")
    print(f"Total profit: {round(overall_value,2)}")
    print(f"First Buy: {first_buy}")
    print(f"% return: {round(final_profit_percentage, 2)}")


def meanReversion(openfile):
    # link file
    file = open(openfile)
    lines = file.readlines()

    # set values of buy, sell, overall_value, average, total
    buy = 0
    sell = 0
    overall_value = 0
    average = 0
    returns = 0
    numreturns = 1
    # list to hold the prices
    price_lst = []
    for line in lines:
        price = float(line)
        price = round(price, 2) # to round the price
        price_lst.append(price)

    # iterate through the list
    for i in range(len(price_lst)):
        current_price = price_lst[i]
        if buy == 0:
                first_buy = current_price
        current_price = price_lst[i]
        #calc returns
        returns += current_price
        #calc numreturns
        numreturns += 1
        average = returns/numreturns
        if price < average:
            # buy
            buy = current_price
            print(f"buy at:      {buy}")

        elif current_price < average:
            # sell
            sell = current_price
            print(f"sell at: {sell}")

            # calculate the amount earned
            trade_value = sell - buy
            print(f"Trade Value:        {trade_value}")
            overall_value += trade_value
        else:
            #pass
            overall_value += 0
    final_profit_percentage = (overall_value / first_buy) * 100
    print("----------------------")
    print(f"Total profit: {round(overall_value, 2)}")
    print(f"First Buy: {first_buy}")
    print(f"% return: {round(final_profit_percentage, 2)}")

def saveResults(results, name, info):
     dictionary = results
     key = name + "_prices"
     dictionary[key] = info           
            

        
# show the moving average for each stock
tickers = ["/workspaces/Data_3500_Homework/HW5/AAPL.txt","/workspaces/Data_3500_Homework/HW5/ADBE.txt","/workspaces/Data_3500_Homework/HW5/ANDE.txt","/workspaces/Data_3500_Homework/HW5/BLK.txt","/workspaces/Data_3500_Homework/HW5/COKE.txt","/workspaces/Data_3500_Homework/HW5/GOOG.txt","/workspaces/Data_3500_Homework/HW5/NTDOF.txt","/workspaces/Data_3500_Homework/HW5/NVDA.txt","/workspaces/Data_3500_Homework/HW5/PEP.txt","/workspaces/Data_3500_Homework/HW5/RIOT.txt"]
ticker_name = ["AAPL", "ADBE", "ANDE", "BLK", "COKE", "GOOG", "NTDOF", "NVDA", "PEP", "RIOT"]

# create dictionary
results = {}

for i in range(len(tickers)):
    print(f"{ticker_name[i-1]} Simple Moving Average")
    simpleMovingAvg(tickers[i-1])
    print(f"{ticker_name[i-1]} Mean Reversion")
    meanReversion(tickers[i-1]) 

saveResults(results, ticker_name[i-1], tickers[i-1])       