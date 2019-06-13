#For loops

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)
    
for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    
print(list_sum)


mystring = 'Hello World'
for letter in mystring:
    print(letter)

# when you don't plan to use the var    
for _ in 'Hello World':
    print('Cool!')
    
tup = (1,2,3)

for item in tup:
    print(item)
    
mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for item in mylist:
    print(item)
    
#a better approach for tuples is:
for a,b in mylist:
    print(a)
    print(b)
    
mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(b)

d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(value)
