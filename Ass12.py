# 1.Create a custom math module and import it in another file. 
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b 

# 2.Create a module to perform string operations.
# String Operations

def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string: ")

print("Uppercase:", to_upper(text))
print("Lowercase:", to_lower(text))
print("Reversed:", reverse_string(text))

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")


# 3.Use random module to generate 5 random integers. 

import random

for _ in range(5):
    print(random.randint(1, 100))


# 4.Use datetime module to display current date and time. 
from datetime import datetime

now = datetime.now()

print("Current Date and Time:", now)

# 5.Create a package shapes with modules for circle and rectangle.

import math

def circle_area(r): return math.pi * r**2
def circle_circ(r): return 2 * math.pi * r

def rect_area(l, w): return l * w
def rect_perimeter(l, w): return 2 * (l + w)

choice = input("Choose 1.Circle 2.Rectangle: ")
if choice == "1":

    r = float(input("Radius: "))
    print("Area:", round(circle_area(r),2))
    print("Circumference:", round(circle_circ(r),2))

elif choice == "2":

    l = float(input("Length: "))
    w = float(input("Width: "))
    print("Area:", rect_area(l,w))
    print("Perimeter:", rect_perimeter(l,w))
else:
    print("Invalid choice")

# 6.Create a package shapes with modules for circle and rectangle.

import math

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

# rectangle 

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

# 7.Import multiple functions from one module and use them. 
   # math_ops.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

# 8.Write a program to shuffle a list using random module. 

import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

print("Shuffled list:", my_list)

# 9.Write a program to calculate the difference between two dates.
from datetime import date

d1 = date(2024, 1, 1)
d2 = date(2024, 1, 15)

difference = abs(d2 - d1)

print("Difference in days:", difference.days)

#  10.Use os module to list files in a directory.
import os

path = "."

files = os.listdir(path)
print(files)
