#class: A Class is like an object constructor, or a "blueprint" for creating objects.
#Object: Almost everything in Python is an object, with its properties and methods.

class MyFamily:  #this is a simplest form of creating a class
    name = "Megha Ahirwar"
    age = 23
    weight = 42.5
    girl = True
    
m = MyFamily()  #Creating an onject
print(m.name)   #accessing the data whatever inside the class
print(m.age)
print(m.weight)
print(m.girl)

# class with init() function
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
#Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Fruits:
  def __init__(self, fruit_name, fruit_color):
    self.fruit_name = fruit_name
    self.fruit_color = fruit_color

p1 = Fruits("Apple", "brown")
print(p1.fruit_name)
print(p1.fruit_color)

#Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

