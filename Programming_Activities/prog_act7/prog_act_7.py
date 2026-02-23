"""
Programming Activity 1

Write a program, and have the user enter their name and their favorite 
color, as two separate variables. Write the sentence to a file using the 
with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""
"""
import numpy

# ask user for name and fav color convert to array
name = input("What is your name: ")
color = input("What is your favorite color: ")
userInfo = [name, color]

# convert to numpy array
userInfoPy = numpy.array(userInfo)

# write to a file
userInfoPy.tofile("prog_act_7_test")

# test if it went to array
print(userInfoPy)

# retrive sentence from a file
from Programming_Activities.prog_act7 import prog_act_7_test
outfile = prog_act_7_test

print(outfile)
"""

"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""
import numpy

numarray = []
for i in range(100):
    numarray.append(0)
numpy.array(numarray)
print(numarray)

for j in range(100):
    numarray[j] = round(numpy.random.rand(), 2)
print(numarray)