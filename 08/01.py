#OOP Attributes and Class keyword

mylist = [1,2,3]

myset = set()

print(type(myset))

class Dog():
    
    def __init__(self,breed,name, spots):
        
        # Attributes
        # We take in the argumnent
        # Assing it using self.attribute_name
        self.breed = breed
        self.name = name
        
        # Expect booleand True/False
        self.spots = spots
        
my_dog = Dog(breed='Lab',name='Sammy',spots=False)

print(type(my_dog))
        
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

