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
print("Value of name", dictionary["Name"])
print("Value of Age", dictionary["Age"])

print("-------------------------------------------------")

#Removing elements from Dictionary
print("Removing elements from Dictionary")
dictionary = {'Name': 'Megha', 'Age': 24, 'weight': 43.2}
print("initial dictionary: ", dictionary)

del dictionary["weight"]    #del keyword is used to delete an element from the dictionary
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