# I/O

myfile = open('myfile.txt')

#myfile = open('opp')

print(myfile.read())

print(myfile.read())

print(myfile.seek(0))

contents = myfile.read()

print(contents)

print(myfile.seek(0))

print(myfile.readlines())

myfile.close()

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    
print(contents)

with open('myfile.txt',mode= 'r') as myfile:
    contents = myfile.read()
    
print(contents)

with open('my_new_file.txt',mode='r') as f:
    print(f.read())
    
with open('my_new_file.txt',mode='a') as f:
    f.write('\nFOUR ON FOURTH')
    
with open('my_new_file.txt',mode='r') as f:
    print(f.read())
    
with open('asdfaffsafs.txt',mode='w') as f:
    f.write('I CREATED THIS FILE!')
    
with open('asdfaffsafs.txt',mode='r') as f:
    print(f.read())
