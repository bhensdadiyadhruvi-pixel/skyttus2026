# 1.Calculate the remainder of two numbers.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:: "))

remainder = num1 % num2

print("The remainder is:", remainder)

#  2.Check if a number is even or odd.
num=int(input("Enter a number :"))
if num % 2==0:
     print("The Number is Even:")
else:
     print("The NUmber is odd:")

#  3.Compare two numbers and print the larger one.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal")

# 4 Write a program to calculate the square and cube of a number.

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square of the number:", square)
print("Cube of the number:", cube)

# Take input from the user
num = int(input("Enter a number: "))

# Calculate square and cube
square = num ** 2
cube = num ** 3

# Display results
print("Square of the number:", square)
print("Cube of the number:", cube)

# 5 Check if two entered numbers are equal.
num1=int(input("Enter first number :"))
num2=int(input("Enter Second number:"))

if num1==num2:
    print("Both number are equal:")
else:
    print("Both number are not equal:")

# 6.Take two numbers and print True if both are positive, else False.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

result = num1 > 0 and num2 > 0

print(result)

# 7.Write a program to convert float to integer.


num = float(input("Enter a float number:"))

int_num = int (num)

print("Integer Value:",int_num)

# 8.Take a number as string, convert to int, and multiply by 10.

num_str = input ("Enter a number:")

num = int (num_str)

result = num * 10 


print("Result:",result)


# 9 Write a program that uses and & or operators to check multiple conditions.
num = int (input ("Enter a number:"))


if num > 0 and num % 2 == 0:
    print("Number is positive and even")

elif num < 0 or num % 2 !=0:

    print("Numbee is negative or odd")
else:

    print("Number is zero")

 # 10.Divide two numbers and print the quotient and remainder separately.	

num1 = int(input("Enter the first number:"))
num2 = int(input ("Enter the second number:"))


quotient = num1 // num2
remainder = num1 % num2

print("Quotient:",quotient)
print("Remainder:",remainder)


