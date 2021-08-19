from itertools import permutations
import pyautogui, sys
import time
import random
import hashlib 

string = 'aa69c940da2cfa075cf4b7f4addd6942'
wordsupper = [] #keywords that you want to use
wordslower = [x.lower() for x in wordsupper]
allwords = wordslower+wordsupper
print(allwords)


#-----------------------------------------------------------------------------------

def compare8(words,string):

    print('length 8 words')

    #with space in between
    print('hello')
    for word in [' '.join(s) for s in permutations(words,8)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

        
    #with underscore in between
    for word in ['_'.join(s) for s in permutations(words,8)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


    #with nothing in between
    for word in [''.join(s) for s in permutations(words,8)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


#-----------------------------------------------------------------------------------

def compare7(words,string):

    print('length 7 words')

    #with space in between
    for word in [' '.join(s) for s in permutations(words,7)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

        
    #with underscore in between
    for word in ['_'.join(s) for s in permutations(words,7)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


    #with nothing in between
    for word in [''.join(s) for s in permutations(words,7)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


#-----------------------------------------------------------------------------------

def compare6(words,string):


    print('length 6 words')
    #with space in between
    for word in [' '.join(s) for s in permutations(words,6)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

        
    #with underscore in between
    for word in ['_'.join(s) for s in permutations(words,6)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


    #with nothing in between
    for word in [''.join(s) for s in permutations(words,6)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


#-----------------------------------------------------------------------------------

def compare5(words,string):
    
    print('length 5 words')

    #with space in between
    for word in [' '.join(s) for s in permutations(words,5)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

        
    #with underscore in between
    for word in ['_'.join(s) for s in permutations(words,5)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


    #with nothing in between
    for word in [''.join(s) for s in permutations(words,5)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


#-----------------------------------------------------------------------------------

def compare4(words,string):

    print('length 4 words')

    #with space in between
    for word in [' '.join(s) for s in permutations(words,4)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

        
    #with underscore in between
    for word in ['_'.join(s) for s in permutations(words,4)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


    #with nothing in between
    for word in [''.join(s) for s in permutations(words,4)]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

#-----------------------------------------------------------------------------------

def compareall(words,string):

    print('length 4 words')

    #with space in between
    for word in [' '.join(s) for s in permutations(words,len(words))]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)

        
    #with underscore in between
    for word in ['_'.join(s) for s in permutations(words,len(words))]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


    #with nothing in between
    for word in [''.join(s) for s in permutations(words,len(words))]:
        #hash md5
        result = hashlib.md5(word.encode()) 
        generated = result.hexdigest()
        if generated == string:
            print(f'THIS IS THE ONE -- {word}')
            break
        else:
            print(generated)


compare4(allwords,string)
compare5(allwords,string)
compare6(allwords,string)
compare7(allwords,string)
compare8(allwords,string)
compareall(allwords,string)
