# Programming Activity 1
apple_price = 10
number_purchased = 5
tax = 1.07
total_bill = apple_price * number_purchased * tax
print(f"Apples purchased: {number_purchased}")
if total_bill != 0:
    print(f"Total bill: {total_bill}")
else:
    print("check inputs")

# Programming Activity 2
age = float(input("How old are you: "))
death_age = float(input("How old do you want to live to: "))
print(f"You have {death_age - age} years left to live.")

# Programming Activity 3
score = float(input("What is your grade percentage: "))
if score >= 93:
    print("Congratulations you got an A")
else:
    print("Congratulations, you still learned a ton!!!!")