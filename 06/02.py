# Functions

def name_function():
    '''
    DOCSTRING: Information about the Functions
    INPUT: no input...
    OUTPUT: Hello ..
    '''
    print('Hello')
    
#help(name_function )

def say_hello(name='Jose'):
    return 'hello ' + name
    
result = say_hello('David')

print(result)

def add(n1,n2):
    return n1 + n2

result = add(20,30)

print(result)

# find out if the word "dog" is in a string
def dog_check(mystring):
    return 'dog' in mystring.lower()
    
print(dog_check('Dog ran away'))

# PIG LATIN
#
# If word starts with a vowel, add 'ay' to end
# If word does not start with a vowel, put first letter at the end, then add 'ay'
# word --> ordway
# apple--> appleay

def pig_latin(word):
    first_letter = word[0]
    
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
        
    return pig_word
    
print(pig_latin('apple'))
print(pig_latin('word'))
    
