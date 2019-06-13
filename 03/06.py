#Formatting with the .format() method

print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox','brown','quick'))

# To make grammatical sense
print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#Float formatting follows "{value:width.precision f}"

result = 100/777

print(result)

print('The result was {r:1.5f}'.format(r=result))

result = 104.12345

print(result)

print('The result was {r:1.5f}'.format(r=result))

#Other formatting method

name = 'Jose'

print(f'Hello, his name is {name}')

name = 'Sam'
age = 3

print(f'{name} is {age} years old.')
