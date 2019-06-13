# Useful operators

# RANGE
mylist = [1,2,3]

for num in range(0,11,2):
    print(num)
        
print(list(range(0,11,2)))

#enumerate

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

for index,item  in enumerate('abcde'):
    print(item)
    print(index)
    
#ZIP

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in  zip(mylist1,mylist2,mylist3):
    print(item)
    
# in
print('x' in [1,2,3])

print('a' in 'a world')

print('mykey' in {'mykey':345})

d = {'mykey':345}

print(345 in d.keys())

# min and max
mylist = [10,20,30,40,100]

print(min(mylist))

print(max(mylist))

#random
from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)

print(mylist)

from random import randint

print(randint(0,100))

# input

result = input('Enter a number here: ')

print(type(result))
print(int(result))



