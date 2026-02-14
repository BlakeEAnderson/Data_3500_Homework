"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""
"""
colors = ['Purple', 'Green', 'Pink']
for i in range(len(colors)):
    print(colors[i])
"""

"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""
"""
colors = ['Purple', 'Green', 'Pink']
for i in range(len(colors)):
    for j in colors[i]:
        print(j)
"""

"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
"""
import random
randList = []
for i in range(10):
    randnum = random.randint(1, 100)
    randList.append(randnum)

for i in range(len(randList)):
    print(randList[i])
"""
"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""
"""
import random
randList = []
for i in range(10):
    randnum = random.randint(1, 100)
    randList.append(randnum)

for i in range(len(randList)):
    if randList[i] % 2 == 0 and randList[i + 1] % 2 == 0:
        print(randList[i])
        print(randList[i + 1])
"""
"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""
file = open("/workspaces/Data_3500_Homework/Programming_Activities/AAPL.2023.txt")

lines = file.readlines()

# blank list to hold the prices
priceList = []

for line in lines:

    price = float(line)

    # to round the price to 2 decimals
    price = round(price, 2)

    #append the rounded price to the list
    priceList.append(price)

# to hold total
totalPrice = 0.0

# adds every number into totalPrice
for i in range(len(priceList)):
    totalPrice += priceList[i]

# takes totalPrice and divides it by the amount of numbers in priceList
avgPrice = totalPrice/len(priceList)
print(f"The avg of all days is {round(avgPrice, 2)}")

# reset total
totalPrice = 0

#counter variable
j = 0
while j < 5:
    totalPrice += priceList[i]
    j += 1

# takes totalPrice and divides it by the amount of numbers in priceList
fiveDayAvgPrice = totalPrice/len(priceList)
print(f"The avg of first five days is {round(fiveDayAvgPrice, 2)}")