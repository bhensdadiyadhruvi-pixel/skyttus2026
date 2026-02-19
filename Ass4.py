# 1.Create a tuple with 5 numbers. 
numbers = (10,20,30,40,50)
print(numbers)

# 2.Access the third element in a tuple.
my_tuple = (10,20,30,40,50)
print(my_tuple[2])

# 3.Unpack a tuple into separate variables.
my_tuple = (10,20,30,40)
a ,b , c ,d=my_tuple

print(a)
print(b)
print(c)
print(d)

#  4.Create a set of 5 fruits.
fruits = {"Apple","Banana","Kiwi","orange","Grapes"}
print(fruits)

# 5.Add a new fruit to the set.

fruits = {"Apple","Banana","Kiwi","orange","Grapes"}
fruits.add("pineapple")
print(fruits)

# 6.Remove an element from a set. 
fruits = {"Apple","Banana","Kiwi","orange","Grapes"}
fruits.remove("Banana")
print(fruits)

# 7.Find union of two sets.
set1={1,2,3}
set2={3,4,5}

union_set = set1 | set2
print(union_set)

# 8.Find intersection of two sets.
set1={1,2,3}
set2={3,4,5}

intersection_set = set1 & set2
print(intersection_set)

# 9.Check if one set is subset of another.
set1 = {1,2}
set2 ={1,2,3,4}

print(set1.issubset(set2))

# 10. Convert a list with duplicate values into a set to remove duplicates.

my_list = [1,2,3,2,4,4,5]

unique_set = set(my_list)
print(unique_set)


# 11.Create a dictionary storing student names and marks.

students = {
    "Dhruvi": 85,
    "Kirtan": 90,
    "Jenny": 78,
    "jay": 92
}

print(students)

# 12.Add a new key-value pair to an existing dictionary.
students = {
    "Dhruvi": 85,
    "Kirtan": 90,
    "Jenny": 78
}

students["jay"] = 91

print(students)

# 13.Delete a key-value pair from a dictionary.

students = {
    "Dhruvi": 85,
    "Kirtan": 90,
    "Jenny": 78
}

del students["Jenny"]

print(students)

# 14.Merge two dictionaries into one. 

dict1 = {"Dhruvi": 85, "kirtan": 90}
dict2 = {"Jenny": 78, "jay": 92}

dict1.update(dict2)
print(dict1)

# 15.Check if a key exists in a dictionary.
students = {
    "Dhruvi": 85,
    "kirtan": 90,
    "jenny": 78
}

print("kirtan" in students)
print("jay" in students)

# 16.Count word frequency in a given string using a dictionary.

text = "python is easy and python is powerful"

words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# 17.Find the key with the maximum value in a dictionary.
students = {
    "Dhruvi": 85,
    "kirtan": 90,
    "Jenny": 78,
    "jay": 92
}

max_key = max(students, key=students.get)

print(max_key)

# 18.Reverse keys and values in a dictionary. 

students = {
    "Dhruvi": 85,
    "kirtan": 90,
    "Jenny": 78
}

reversed_dict = {value: key for key, value in students.items()}

print(reversed_dict)

# 19.Update the value for a specific key.
students = {
    "Dhruvi": 85,
    "kirtan": 90,
    "Jenny": 78
}

students["kirtan"] = 95

print(students)

# 20.Convert a list of tuples into a dictionary.
list_of_tuples = [("Dhruvi", 85), ("kirtan", 90), ("jenny", 78)]

students_dict = dict(list_of_tuples)
print(students_dict)
