# Nested statements and scope

x = 25

def printer():
    x = 50
    return x

print(printer())

print(x)

#local
lambda num: num ** 2

# Global
name = 'THIS IS A GLOBAL STRING'

def greet():
    #Enclosing
    name = 'Sammy' 
    
    def hello():
        #local
        name = 'Im a local'
        print('Hello ' + name)
        
    hello()
    
greet()


x  = 50

def func(x):    
    print(f'X is {x}')
    
    # Local reassigment
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')
    
func(x)

print(x)
