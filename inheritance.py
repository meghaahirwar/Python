#Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#creating a child class
class Student(Person):
  pass


#creating an object to child class and accessing the data from the parent class
x = Student("Mike", "Olsen")
x.printname()