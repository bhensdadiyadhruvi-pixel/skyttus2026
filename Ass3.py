# 1.Take a string input and print its length.
s= input("Enter a string:")
print(len(s))

# 2.Convert a sentence to lowercase.
sentence = input ("Enter a sentence:")
print(sentence.lower())

# 3.Replace spaces with underscores in a string.
text = input ("enter a string:")
print(text.replace(" ","_"))

# 4.Extract the first and last character of a string.
text = input ("Enter a string:")
print("First character:", text[0])
print("Last character:", text[-1])

#  5.Reverse a string using slicing. 
s=input("Enter a string:")
print(len(s))

# 6.Count how many times a letter appears in a string.
s=input("Enter a string:")
ch= input("Enter a letter to count:")
count = s.count(ch)

print(count)
# 7.Check if a word is present in a sentence. 

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word is present")
else:
    print("Word is not present")

#  8.Take name & age and print using f-string formatting. 
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")

# 9.Remove extra spaces from the start and end of a string. 


text = input ("Enter a string:")

clean_text = text.strip


print(f"After removing spaces: '{clean_text}'")

# 10.Join a list of words into a single string with - between them.
words = ["Python", "is", "easy", "to", "learn"]

result = "-".join(words)
print(result)

#  11.Create a list of your 5 favorite movies.

favorite_movies = [
    "3 Idiots",
    "The lion king",
    "Frozen",
    "Avengers: Endgame",
    "Dangal"
]

print(favorite_movies)

# 12. Add a new movie to the list. 

favorite_movies = [
    "3 Idiots",
    "Moana",
    "Cinderella",
    "Avengers: Endgame",
    "Dangal"
]

favorite_movies.append("Bahubali")

print(favorite_movies)

# 13. Remove the first movie from the list.
favorite_movies = [
   " 3 Idiots",
    "The lion king",
    "Frozen",
    "Avengers: Endgame",
    "Dangal"
]

favorite_movies.pop(0)

print(favorite_movies)

# 14.Sort a list of numbers in ascending order. 
numbers = [10,12,30, 6, 90, 21]

numbers.sort()

print(numbers)

# 15 Reverse a list. 

numbers = [1,2,3,4,5]

numbers.reverse()

print(numbers)

# 16.Find the largest number in a list. 

numbers =[12,60,40,7,80,10]

largest = max(numbers)
print("largest number :", largest)

# 17.Merge two lists into one.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2

print(merged_list)

# 18.Access the last element of a list without using index number.
numbers = [10, 20, 30, 40, 50]

last_element = numbers[-1]

print(last_element)

#  19.Create a nested list and access a specific inner element. 
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element = nested_list[1][1]

print(element)

# 20.Count how many times an element appears in a list.

numbers = [1,2,3,4,5,4]

count = numbers.count(2)
print("2 appears", count, "times")