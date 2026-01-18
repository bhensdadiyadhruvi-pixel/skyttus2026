# 1.Write a program to read a file and display its contents. 
try:
    file = open("example.txt", "r")  
    content = file.read()            
    print(content)
    file.close()                    
except FileNotFoundError:
    print("File not found")

# 2.Write a program to count the number of lines in a file.
try:
    with open("example.txt", "r") as file:  
        lines = file.readlines()            
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found")

# 3.Write a program to count how many times each word appears in a file.

from collections import Counter

try:
    with open("example.txt", "r") as file:
        text = file.read().lower()       
        words = text.split()              
        word_count = Counter(words)       

    for word, count in word_count.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("File not found")

# 4.Write a program to write 5 user-entered sentences to a file.
with open("sentences.txt", "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")

print("Sentences written to file successfully.")

# 5 Write a program to append a list of strings to an existing file. 
strings = ["Hello\n", "Python\n", "File Handling\n"]

with open("example.txt", "a") as file:
    file.writelines(strings)

print("Strings appended to file.")

# 6.Write a program to read a file and print only lines containing a specific word. 
strings = ["Hello\n", "Python\n", "File Handling\n"]

with open("example.txt", "a") as file:
    file.writelines(strings)

print("Strings appended to file.")

# 7.Write a program to replace a specific word in a file and save changes.
try:
    with open("example.txt", "r") as file:
        content = file.read()

    content = content.replace("oldword", "newword")

    with open("example.txt", "w") as file:
        file.write(content)

    print("Word replaced successfully.")

except FileNotFoundError:
    print("File not found")

# 8.Write a program to merge the contents of two text files into a third file.
try:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    with open("merged.txt", "w") as f3:
        f3.write(content1 + "\n" + content2)

    print("Files merged successfully.")

except FileNotFoundError:
    print("One or more files not found")

# 9.Write a program to read a CSV file and display its content in a formatted way
import csv

try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
except FileNotFoundError:
    print("CSV file not found")

#  10.Write a program to back up a file by copying its contents into another file.
try:
    with open("original.txt", "r") as src:
        data = src.read()

    with open("backup.txt", "w") as dest:
        dest.write(data)

    print("Backup created successfully.")

except FileNotFoundError:
    print("Source file not found")
