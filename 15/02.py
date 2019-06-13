#defaultdict

from collections import defaultdict

d = {'k1':1}

d['k1']

# shows error
#d['k2']
    
d = defaultdict(object)

print(d['one'])

for item in d: 
    print(item)
    
d = defaultdict(lambda: 0)

print(d['one'])

d['two'] = 2

print(d['two'])
