# 1.Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
try:
    with open("original.txt", "r") as src:
        data = src.read()

    with open("backup.txt", "w") as dest:
        dest.write(data)

    print("Backup created successfully.")

except FileNotFoundError:
    print("Source file not found")

#  2.Create a BankAccount class with deposit and withdraw methods.
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
        print("Balance:", self.balance)

account = BankAccount("Dhruvi", 40000)
account.deposit(500)
account.withdraw(300)

# 3.Create a Student class with a method to calculate average marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # list of marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Asha", [80, 75, 90])
print("Average marks:", s1.average())

#  4.Create a Rectangle class with methods to find area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

# 5.Create an Employee class that displays salary details.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


e = Employee("dhruvi", 35000)
e.show_salary()

# 6.Create a Book class to store title, author, and price, and display details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b = Book("Python Basics", "John Smith", 500)
b.display()

# 7.Create a Circle class to find area and circumference.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(7)
print("Area:", round(c.area(), 2))
print("Circumference:", round(c.circumference(), 2))

# 8. Create a Laptop class with a method to apply discounts on price.
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100
        print("Price after discount:", self.price)


l = Laptop("Hp", 60000)
l.apply_discount(10)

# 9.Create a Flight class with seat booking functionality. 
class Flight:
    def __init__(self, flight_no, seats):
        self.flight_no = flight_no
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked successfully")
        else:
            print("No seats available")

# Example usage
f = Flight("AI202", 2)
f.book_seat()
f.book_seat()
f.book_seat()

# 10.Create a Shop class with a method to add and list products.

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"'{product}' added to shop.")

    def list_products(self):
        print("Products in shop:", ", ".join(self.products))

shop = Shop("MyStore")
shop.add_product("Laptop")
shop.add_product("Mouse")
shop.list_products()
