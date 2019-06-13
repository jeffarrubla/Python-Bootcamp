# OOP Inheritance and Polymorphism 

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print('I am an animal')
        
    def eat(self):
        print('I am eating')
     
     
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self) 
        print("Dog Created")
  
    def eat(self):
        print('I am a dog and eating')
        
    def bark(self):
        print("WOOF!")

mydog = Dog()

mydog.eat()

mydog.bark()

myanimal = Animal()

myanimal.eat()

myanimal.who_am_i()

#Polymorphism

class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says  meow!"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())

print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(niko)

pet_speak(felix)

#Abstract class

class Animal():
     
    def __init__(self,name):
         self.name = name
         
    def speak(self):
        raise NotImplementedError("Subclass must implemement this abstract method")
    
class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof!"
       
class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"
    
fido = Dog("Fido")
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


