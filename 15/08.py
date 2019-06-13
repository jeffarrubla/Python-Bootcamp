# Regular expressions

import re

patterns = ['term1','term2']

text = 'This is a string with term1, but no the other term'

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('\n')
        print('March was found. \n')
    else:
        print('\n')
        print('No March was found. \n')
        
match = re.search(patterns[0],text)

print(type(match))
        
print(match.start())

print(match.end())

split_term = '@'

phrase = 'What is your email, it is hello@gmail.com?'

print(re.split(split_term,phrase))

print(re.findall('match','Here is one match, here is another match'))

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',     # s followed by zero or more d's
                 'sd+',     # s followed by one or more d's
                 'sd?',     # s followed by zero or one d's
                 'sd{3}',   # s followed by three d's
                 'sd{2,3}'  # s followed by two to three d's
    ]

multi_re_find(test_patterns,test_phrase)

test_patterns = ['[sd]',        # either s or d
                 's[sd]+' ]     # s followed bt one or more s or d

multi_re_find(test_patterns,test_phrase)



