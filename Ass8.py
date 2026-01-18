# 1.Function to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 2.Function to reverse a string.
def reverse_string(s):
    return s[::-1]

# 3.Function to find factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

#  4.Function to calculate simple interest.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest (%): "))
t = float(input("Enter time (years): "))

si = simple_interest(p, r, t)
print(f"Simple Interest is: {si}")

# 5.Function to check if a word is palindrome. 
def is_palindrome(word):
    return word == word[::-1]

text = input("Enter a word: ")
if is_palindrome(text):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")

# 6.Function to count vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

# 7.Function to merge two lists.

def merge_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = merge_lists(list1, list2)
print("Merged list:", merged)

# 8.Function to find GCD of two numbers.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"GCD of {x} and {y} is {gcd(x, y)}")

#  9.Function to find area of rectangle. 
def rectangle_area(length, width):
    return length * width


l = float(input("Enter length: "))
w = float(input("Enter width: "))
print("Area of rectangle:", rectangle_area(l, w))

# 10.Function to check Armstrong number.
n = int(input("Enter number: "))
print("Armstrong" if n == sum(int(d)**len(str(n)) for d in str(n)) else "Not Armstrong")
