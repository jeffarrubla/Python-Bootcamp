# OOP Class object attributes and methods 

class Dog():
    
    # CLASS OBJECT ATTRIBUTE 
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    
    def __init__(self,breed,name):
        
        # Attributes
        # We take in the argumnent
        # Assing it using self.attribute_name
        self.breed = breed
        self.name = name        
        
    # OPERATIONS/Actions --> Methods
    def bark(self,number):
        print('WOFF! My name is {} and the number is {}' .format(self.name,number))
        
my_dog = Dog('Lab','Sammy')


print(type(my_dog))
        
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

my_dog.bark(10)

class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        
    # METHOD 
    def get_circumference(self):
        return self.radius * Circle.pi * 2
    
my_circle = Circle(30)

print(my_circle.pi)

print(my_circle.radius)

print(my_circle.get_circumference())
