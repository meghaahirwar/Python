#List data type
#Definition: List is a ordered sequens of an elements, it is an mutable data type in the python and also most used in python.
# we can perform update , delete operations in the list.  it can store any type of value and it is defined within square[] bracket

print("************* LIST Output: ***************") 
# A list with 3 integers
print("List with integers: ")
numbers = [1, 2, 5]
print(numbers)  # Output: [1, 2, 5]

print("Empty List: ")
# empty list
my_list = []
print(my_list)

print("List with mixed data type: ")
# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)

print("-------------------------------------------------")

print("Accessing List items using index: ")
languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[0])   # Python

# access item at index 2
print(languages[2])   # C++

print("-------------------------------------------------")

print("Accessing List items using negetive index: ")
languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[-1])   # C++

# access item at index 2
print(languages[-3])   # Python

print("-------------------------------------------------")

# List slicing in Python
print("Slicing list items: ")
my_list = ['p','r','o','g','r','a','m','i','z']

# items from index 2 to index 4
print("items from index 2 to index 4: ")
print(my_list[2:5])

# items from index 5 to end
print("items from index 5 to end: ")
print(my_list[5:])

# items beginning to end
print("items beginning to end: ")
print(my_list[:])

print("-------------------------------------------------")

print("Adding an element to a list using append() method: ")
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)

# using append method
numbers.append(32)

print("After Append:", numbers)

print("-------------------------------------------------")

print("Adding an element to a list using extend() method: ")
prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

# join two lists
prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers) 

print("-------------------------------------------------")

print("Insert an element to a list in the specified index using insert() method: ")
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')
print('List:', vowel)

print("-------------------------------------------------")

print("Change list items: ")
languages = ['Python', 'Swift', 'C++']
print("Befor changing: ", languages)
# changing the third item to 'C'
languages[2] = 'C'

print("After changing: ", languages)  # ['Python', 'Swift', 'C']

print("-------------------------------------------------")
print("Remove an element from the list: ")
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

# delete first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)

print("-------------------------------------------------")

print("Remove an element from the list using remove() method: ")
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')   #it's uses values

print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

print("-------------------------------------------------")

print("Remove an element from the list using pop() method: ")
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]   

# remove the element at index 2
removed_element = prime_numbers.pop(2)   #its uses indexes

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# Output: 
# Removed Element: 5
# Updated List: [2, 3, 7]

print("-------------------------------------------------")
print("pop() without an index, and for negative indices: ")
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:') 
print('Return Value:', languages.pop())

print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))

print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))

print('Updated List:', languages)
print("-------------------------------------------------")

print("List Count: ")
# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

# check the count of 2
count = numbers.count(2) 

print('Count of 2:', count)

print("-------------------------------------------------")

print("Iterating through a List: ")
languages = ['Python', 'Swift', 'C++']

# iterating through the list
for language in languages:
    print(language)
    
print("--------------------------------------------------")

print("Check if an Item Exists in the Python List: ")   
languages = ['Python', 'Swift', 'C++']

print('C' in languages)    # False
print('Python' in languages)    # True

print("-------------------------------------------------")

print("Python List Length: ") #len() is used to find length of the list
languages = ['Python', 'Swift', 'C++']

print("List: ", languages)

print("Total Elements: ", len(languages))    # 3

print("-------------------------------------------------")

