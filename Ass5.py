# 1.Print numbers from 1 to 10. 
for i in range(1,11):
    print(i)

# 2.Display multiplication table for a given number. 
num = 19  # change this to any number

for i in range(1,11):
    print(f"{num} x {i} = {num * i }")

# 3.Find factorial of a number.
num = 5  # change this to any number
factorial = 1

for i in range(1,num + 1):
    factorial *=i
print(f"Factorial of {num} is {factorial}")

# 4.Generate the first N Fibonacci numbers.   
N= 10 
  
fib = [0,1]
for i in range(2,N):

    next_number = fib [i-1] + fib[i-2]

    fib.append(next_number)

print(fib[:N])

# 5.Check if a number is prime.
num = 6  # change this to any number

if num > 1:
    for i in range(2, int (num**0.5)+1):
         if num % 1 == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")

#  6.Reverse a number (e.g., 123 → 321).
num = 123 
reversed_num = int (str(num)[::-1])
print(reversed_num)

# 7.Count digits in a number. 
num = 12345
num_digits = len (str(num))
print(num_digits)

# 8.Find sum of even numbers between 1–100.
total = 0

for i in range(2,101,2):
     total += i
print(total)

#  9.Print a pyramid pattern.   
rows = 5

for i in range(1, rows +1):
    
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

#  10.Find all divisors of a number.	
num = 24  # Change this to any number
divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print(divisors)
