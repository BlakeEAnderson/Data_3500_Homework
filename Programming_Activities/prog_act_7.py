"""
Programming Activity 1

Write a program, and have the user enter their name and their favorite 
color, as two separate variables. Write the sentence to a file using the 
with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""
import numpy

# ask user for name and fav color
name = input("What is your name: ")
color = input("What is your favorite color: ")

# write sentence to a file
from Programming_Activities import prog_act_7_text
"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""