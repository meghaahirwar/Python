#encapsulation is used for bundling the data member and methods.
#class is an example of encapsulation

class person:
    def __init__(self):
        self.name = "Megha Ahirwar"   #data member
        
    def bio(self):                    #methods or function
        self.address = "Pipariya, Hoshangabad"
        self.taxinfo = "qwrt12356"
        self.contact = 1234567890
        print(self.address, self.taxinfo, self.contact)
        
    def interest(self):
        self.favFood = "Chinese"
        self.hobbies = "painting"
        self.bloodGroup = "B+"
        print(self.favFood, self.hobbies, self.bloodGroup)

obj = person()
print(obj.name)
obj.bio()
obj.interest()