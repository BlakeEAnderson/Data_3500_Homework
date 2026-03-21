# link TSLA.csv
file = open("/workspaces/Data_3500_Homework/HW4/TSLA.txt")
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
    if i <= 247:
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
    elif current_price > moving_avg*1.02:
        # sell stock
        sell = current_price
        print(f"Selling at:     {sell}")

        # calculate the amount earned and add it to the total
        trade_value = sell - buy
        print(f"Trade Value:        {trade_value}")
        overall_value += trade_value
    else:
        # dont buy or sell
        overall_value += 0
final_profit_percentage = (overall_value / first_buy) * 100
print("----------------------")
print(f"Total profit: {overall_value}")
print(f"First Buy: {first_buy}")
print(f"% return: {round(final_profit_percentage, 2)}")