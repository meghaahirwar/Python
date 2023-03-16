print("Hello")
print('Hello')

#Assigning a string to a variable

a = "Hello"
print(a)

#multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#string are array
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "programming":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")