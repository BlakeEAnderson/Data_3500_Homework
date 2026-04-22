# 3.4
for i in range(2):
    for i in range(7):
        print('@', end="")
    print()

# 3.9
# prompt
number = input("Enter a number between 7 and 10 digits: ")

# test if number was given
try:
    int(number)
except:
    print("did not enter a number try again")

# loop through the lenght of the nubmer
for i in range(len(number)):

    # take the inverse of current count
    x = len(number) - (i+1)

    digit = (int(number) % 10 ** (x+1)) // (1 * (10**x))
    print(digit)

#3.11
# variables
gallons = 0
miles = 0
total = 0
while gallons >= 0:
    gallons = float(input("How many gallons used (-1 to end): ")) # asks for gallons used
    if gallons >= 0:
        miles = float(input("Enter the miles driven: "))              # asks for miles driven
        print(f"The miles/gallon for this tank was {miles/gallons}")  # shows the miles per gallon
        total += (miles/gallons)                                      # adds to a running total
        timesRun += 1
print(f"The overall average miles/gallon was {total/timesRun}")

# 3.12
