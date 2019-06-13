# *args and **kwargs

def myfunc(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05
    
print(myfunc(40,60,100,100))

def myfunc1(*args):
    return sum(args) * 0.05

print(myfunc1(40,60,100,1,34))

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc2(fruit='apple',veggi='lettuce')

def myfunc3(*args,**kwargs):
    
    print('I would like {} {}'.format(args[0],kwargs['food']))
    
myfunc3(10,20,30,fruit='orange',food='eggs',animal='dog')

