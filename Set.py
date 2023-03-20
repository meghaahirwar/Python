#Set data type
#Definition: A set is an unordered collection of an items and work on unique values, it only takes unique values and can remove duplicate values.
#this is a immutable data type

print("************* SET Output: ***************") 
print("create a SET in python: ")
#create a set of an integer type
student_id = {101, 102, 103, 104, 105}
print("Integer set: ", student_id)

#create a set of a string type
str_set = {'a', 'e', 'i', 'o', 'u'}
print("String type set: ", str_set)

#create a set of a mixed data type
mixed_set = {1, "Megha", 43.2, -5, True}
print("A set of mixed data type: ", mixed_set)

print("-------------------------------------------------")

#create an empty set
print("Empty set in python: ")
empty_set = set()

#check data type of empty_set
print("Type of empty_set: ", type(empty_set))

# create an empty dictionary
empty_dictionary = { } 

#check data type of empty_dictionary
print("type of empty_set: ", type(empty_dictionary))

print("-------------------------------------------------")

print("Duplicate items in set: ")
Number = {1, 2, 3, 2, 4, 2, 3}
print("Removes duplicate values and takes unique values: ", Number)

print("-------------------------------------------------")

#Add items in set
print("Add items in set: ")
Number = {1, 2, 3, 2, 4, 2, 3}
print("Initial Set: ", Number)

Number.add(6)
print("Updated Set: ", Number)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("-------------------------------------------------")

print("Update set using update() method: ")
#Update set using update() method
#The update() method is used to update the set with items other collection types (lists, tuples, sets, etc). For example,
companies = {'Astoria Solutions', 'Google'}
Tech_companies = ['Apple', 'HCL', 'Infosys', 'IBM']
companies.update(Tech_companies)

print("Updated companies: ", companies)

print("-------------------------------------------------")

#Remove an element from a set
print("Remove an Element from a Set: ")
languages = {'Python', 'Java', 'C', 'C++'}
print("Initial Set: ", languages)

removedValues = languages.discard('Java')
print("Set after removed values: ", languages)

print("-------------------------------------------------")

#Get the largest item in a Set
Number = {1, 3, 6, -3, 9.5, 10}

largest_number = max(Number)
print("Largest Number: ", largest_number) 

print("-------------------------------------------------")

#Get the iteration of the items in a Set
print("Iteration through a Set:")
fruits = {'Apple', 'banana', 'cherry', 'Mango', 'graps'}
for fruit in fruits: 
    print("Iteration: ", fruit)
    
print("-------------------------------------------------")

print("clear() method : ")  #clear() is used to delete all the element from the set
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)



