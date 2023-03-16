class MyFamily:
    name = "Megha Ahirwar"
    age = 23
    weight = 42.5
    girl = True
    
m = MyFamily()
print(m.name)
print(m.age)
print(m.weight)
print(m.girl)


class Fruits:
  def __init__(self, fruit_name, fruit_color):
    self.fruit_name = fruit_name
    self.fruit_color = fruit_color

p1 = Fruits("Apple", "brown")
print(p1.fruit_name)
print(p1.fruit_color)