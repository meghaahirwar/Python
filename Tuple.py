#tuple data type
#Definition: tuple is a ordered sequence of an items same as a list, this is immutable data type in python
# we cannot perform update , delete operations in the tuple.  it can store any type of value
#differnce between list and tuple: this is fast as compared to list, we can access tuple quickly and it is defined within paranthesis()

print("************* TUPLE Output: ***************") 
# Different types of tuples
print("Different types of tuples: ")
# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

print("-------------------------------------------------")
print("Create a Python Tuple With one Element: ")
var1 = ("hello")
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

# Parentheses is optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>

print("-------------------------------------------------")

# accessing tuple elements using indexing
print("accessing tuple elements using indexing: ")
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(letters[0])   # prints "p" 
print(letters[5])   # prints "a"

print("-------------------------------------------------")

# accessing tuple elements using negative indexing
print("Accessing tuple elements using negetive indexing: ")
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # prints 'z' 
print(letters[-3])   # prints 'm'

print("-------------------------------------------------")

# accessing tuple elements using slicing
print("Accessing tuple elements using slicing")
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print("-------------------------------------------------")

#In Python ,methods that add items or remove items are not available with tuple. 
#Only the following two methods are available.
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3

print("-------------------------------------------------")

print("find the length of tuple: ")
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(len(my_tuple))

print("-------------------------------------------------")

print("Iterating through a tuple in python")
languages = ('Python', 'C', 'C++')
for language in languages:
    print(language)
    
print("-------------------------------------------------")
#Check if an Item Exists in the Python Tuple
print("Check if an Item Exists in the Python Tuple")
languages = ('Python', 'C', 'C++')
print('C' in languages)  #True
print('Ruby' in languages) #False

# print("-------------------------------------------------")
# #Check if an Item Exists in the Python Tuple
# print("Check if an Item Exists in the Python Tuple")


# print("-------------------------------------------------")
# #Check if an Item Exists in the Python Tuple
# print("Check if an Item Exists in the Python Tuple")