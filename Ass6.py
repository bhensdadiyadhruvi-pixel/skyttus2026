# 1.Check if a person is eligible to vote (age ≥ 18). 
age = int (input("Enter your age:"))

if age >=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 2.Grade calculator based on marks: 90+ = A, 80+ = B, else C. 

marks = float(input("Enter your marks: "))


if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
else:
    grade = "C"

print(f"Your grade is: {grade}")

# 3.Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go. 

color = input("Enter the traffic light color (Red, Yellow, Green): ").strip().lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid color! Please enter Red, Yellow, or Green.")

# 4.ATM withdrawal check: sufficient balance or not. 

balance = float(input ("Enter your current balance:"))

withdrawal = float(input("Enter amount to withdraw:"))

if withdrawal <= balance:
    balance -= withdrawal
    print(f"Transaction successful! Remaining balance: {balance}")
else:
    print("Insufficient balance! Transaction failed.")

# 5.Check if a number is positive, negative, or zero.


num = float(input ("Enter a number:"))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero. ")


# 6.Check if a number lies within a given range. 

num = float (input("Enter the number:"))
lower = float(input("Enter the lower bound of the range:"))
upper = float(input ("Enter the upper bound of the range:"))

if lower <=num <= upper:
    print(f"{num} lies within the range {lower} to {upper}.")
else:
    print(f"{num} does NOT lie within the range {lower} to {upper}.")

# 7.Username & password verification.
username_db ="user123"
password_db ="pass123"

username = input ("Enter username:")
password = input("Enter password:")

if username == username_db and password == password_db:
    print("Login successful")
else:
    print("Invalid username or password")

# 8.Electricity bill calculator based on units consumed.

units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(f"Total electricity bill = ₹{bill}")

# 9.Simple calculator (add, subtract, multiply, divide). 

num1 = float(input ("Enter First number:"))
num2 = float(input ("Enter second number:"))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")

# 10.Check type of triangle (equilateral, isosceles, scalene).

a = float(input ("Enter First side:"))
b = float(input("Enter second side:"))
c = float(input("ENter third side:"))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    
    print("Isosceles triangle")
else:
    print("Scalene triangle")
