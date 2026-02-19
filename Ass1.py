# 1. Write a program to print your name, age, and city in one line.
name = "Dhruvi"
age = 20
city = "Ahmedabad"

print("Name:", name, "Age:", age, "City:", city)

# 2.Take user input for two numbers and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Sum:", sum)

#3. Write a program to convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 4. Store your name in a variable and print it in uppercase.
name = "Dhruvi"
print(name.upper())

# 5. Ask the user for their birth year and calculate their current age.
birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year
print("Your current age is:", age)

# 6. Write a program to swap the values of two variables.
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# 7. Create a program to calculate the area of a rectangle from user inputs.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print("Area of the rectangle:", area)

# 8. Write a program to check if a number is positive or negative.

num = int(input("Enter a number: "))

if num > 0:
     print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
  print("The number is Zero")

# 9. Ask for two numbers and print their average.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2
print("Average:", average)
