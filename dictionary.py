#Dictionary data type
#Definition: Dictionary data type is an unordered collection of Key-value pairs, dictionary defined within curly-braces{}.
#this is mutable data type.

print("************* DICTIONARY Output: ***************")

print("Create an empty dictionary by using curly {} braces: ")

this_dictionary = {}
print("Empty dictionary: ", this_dictionary)
print("Type of this_dictionary: ", type(this_dictionary))

print("-------------------------------------------------")

print("Creating a dictionary with elements: ")
dict_with_elements = {'Madhya Pradesh': 'Bhopal', 'Telangana': 'Hyderabad'}
print("Created dictionary: ", dict_with_elements)

print("Dictionary with different datatypes: ")
dict_with_diff_dataType = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("Dict with different data type: ", dict_with_diff_dataType)

print("-------------------------------------------------")

#Add element to a python dictionary
print("Adding an element in a dictionary")
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("Initial dictionary: ", dictionary)

dictionary['City'] = 'Bhopal'
print("Updated dictionary: ", dictionary)

print("-------------------------------------------------")

#changing a value of any key
print("Changing a value of any key: ")
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("Initial dictionary: ", dictionary)

dictionary["weight"] = '44 kg'
print("Updated dictionary: ", dictionary)

print("-------------------------------------------------")

#Accessing items from a dictionary
print("Accessing items from a dictionary")
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("Value of name: ", dictionary["Name"])
print("Value of Age: ", dictionary["Age"])

print("-------------------------------------------------")

#Removing elements from Dictionary
print("Removing elements from Dictionary using del keyword: ")
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("initial dictionary: ", dictionary)

del dictionary["weight"]    #del keyword is used to delete an element from the dictionary
print("Updated dictionary: ", dictionary)

print("Using pop() method: ")
#using pop() method : pop() method remove an element with the specified key name from the dictionary
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("initial dictionary: ", dictionary)

dictionary.pop("weight")   #pop() method is used to delete a specified key from the dictionary
print("Updated dictionary: ", dictionary)

print("Using popitem() method: ")
#using popitem() method : popitem() method remove last inserted element from the dictionary
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("initial dictionary: ", dictionary)

dictionary.popitem()   #popitem() method is used to delete last inserted element from the dictionary
print("Updated dictionary: ", dictionary)

print("-------------------------------------------------")

#keys() method in dictionary
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}

dictionary_keys = dictionary.keys()
print(dictionary_keys)

print("-------------------------------------------------")

#values() method in dictionary
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}

dictionary_keys = dictionary.values()
print(dictionary_keys)

print("-------------------------------------------------")

print("clear() method: ")
#clear() method in dictionary
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}

clear_dictionary = dictionary.clear() 
print(dictionary)

print("-------------------------------------------------")
#Print all key names in the dictionary, one by one:
print("Iterating dictionary: ")
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}

for item in dictionary:
     print(item)
     
print("Print all values in the dictionary, one by one: ")
for item in dictionary:
     print(dictionary[item])
     
print("printing keys one by one by using keys() method ")
for key in dictionary.keys():
     print(key)
     
print("printing values one by one by using values() method ")
for value in dictionary.values():
     print(value)
     
print("Loop through both keys and values, by using the items() method: ")
for x,y in dictionary.items():
     print(x,y)
     
print("-------------------------------------------------")

print("Nested dictionary: ")
student_in_class = {'Class1':{
          'Name': 'Jaishree',
          'Roll No.': 101
     },
     'Class2': {
          'Name': 'Anuja',
          'Roll No.': 102
     },
     'Class3': {
          'Name': 'Priya',
          'Roll No.': 103
     }}
print(student_in_class) 

print("To access items from a nested dictionary: ")
print("Items from a Nested dictionary: ", student_in_class['Class2']['Name'])

print("get() method: ")
specified_key = student_in_class.get("Class2")
print(specified_key)

print("-------------------------------------------------")
