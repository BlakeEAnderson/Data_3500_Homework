# Write a Python program, which solves the problems from the book
# 2.3
print("\n 2.3")
grade = 91
if grade >= 90:
    print(f"Your grade of {grade} earns you an A")

# 2.4
print("\n 2.4")
x = 27.5
y = 2
print(f"{x} + {y} = + {(x + y)}")
print(f"{x} - {y} = + {(x - y)}")
print(f"{x} * {y} = + {(x * y)}")
print(f"{x} / {y} = + {(x / y)}")
print(f"{x} // {y} = + {(x // y)}")
print(f"{x} ** {y} = + {(x ** y)}")

# 2.5
print("\n 2.5")
radius = 2
pi = 3.14159
print(f"Diameter = {(2*radius)}")
print(f"Circumference = {(2*pi*radius)}")
print(f"Area = {(pi*(radius**2))}")

# 2.6
print("\n 2.6")
number = 10
if number%2 == 0:
    print("Number is even")
elif number%2 != 0:
    print("Number is odd")

# 2.7
print("\n 2.7")
number = 1024
if 4 % number:
    print(f"{number} is a multiple of 4")
else:
    print(f"{number} is not a multiple of 4")

number = 2
if 10 % number:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

# 2.8
print("\n 2.8")
num = 0
print("Number \t Square \t Cube")
while num <= 5:
    print(f"{num} \t {num**2} \t {num**3}")
    num += 1