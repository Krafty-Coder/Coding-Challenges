class Person:
  version = 0.1
  def __init__(self, name,age):
    self.name = name
    self.age = age
    print("Hello {},".format(self.name))

  def get_age(self):
    """This is gets the age of the object """
    print self.get_age.__doc__
    return self.age

  def __str__(self):
    return self.name, self.age

  def show_version(self):
      print self.__class__.__version__

p = Person('Malcolm', 12)
m = Person('Peter', '67')
print p.__str__()
# print p.get_age()
# p.name
# print m.__str__()
print(type(Person))
print(type(Person.get_age))
print p.show_version()

def pr(name):
  return name

print(type(pr))
