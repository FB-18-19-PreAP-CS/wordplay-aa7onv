
def at_least(): 
    with open("words.txt") as file:
        
        for line in file:
            for word in line.strip().split(' '):
                if len(word) >= 20:
                    print(word)
                    
                       
def has_no_e(word):
    ''' returns True if the given word doesn’t have
the letter “e” in it.
    >>> has_no_e('chickn')
    True
    >>> has_no_e('Elphant')
    False
    >>> has_no_e('apple')
    False
    '''
    
    if 'e' not in word.lower():
        return True
    else:
        return False
                
def no_e(): 
    with open("words.txt") as file:
        count_no_e = 0
        for line in file:
            for word in line.strip().split(' '):
                if has_no_e(line):
                    count_no_e += 1
    
    with open("words.txt") as file:
        num_words = 0
        for line in file:
            for word in line.strip().split(' '):
                num_words += 1
        pct = count_no_e / num_words
        print('{:.2f}%'.format(pct * 100 ))
    
                             
def avoids(word, bad_letters):
    '''  takes a word and a string of forbidden
letters, and that returns True if the word doesn’t
use any of the forbidden letters.
    >>> avoids('dog','qwxc')
    True
    >>> avoids('dog','dta')
    False
    >>> avoids('dog','D ')
    False
    >>> avoids('Texas','tpr')
    False
    >>> avoids('Texas','lmn')
    True
    >>> avoids('Longhorn','LHN')
    False
    >>> avoids('waffle','dre')
    False
    '''
    
    for let in bad_letters:
        for i in range(len(word)):
            if let.lower() == word[i].lower():
                return False
            
    else:
        return True
                       
def count_avoids():
    #abcde = 7990
    forbid_let = input('Enter forbidden letters: ')
 
    with open("words.txt") as file:
        num_words = 0
        for line in file:
            for word in line.strip().split(' '):
                if avoids(line,forbid_let):
                    num_words += 1
    print(num_words)
                
                         
def uses_only(word, str): 
    '''
    >>> uses_only('dog','d')
    False
    >>> uses_only('dog','Dgol')
    True
    >>> uses_only('Texas','tpr')
    False
    >>> uses_only('Texas','tmensxa')
    True
    >>> uses_only('Longhorn','LHN')
    False
    >>> uses_only('waffle','waffle')
    True
    >>> uses_only('cvafef ','adbcefgv ')
    True
    '''
    count = 0
    for i in range(len(word)):
        if word[i].lower() in str.lower():
            count += 1
    if count == len(word):
        return True
    
    return False
    
        
def words_with_only(string):
    with open("words.txt") as file:
        for line in file:
            #for word in line.strip().split():
            if uses_only(line.strip(),string):
                print(line)
            
def uses_all(word,string):
    '''
    >>> uses_all('dog','dog')
    True
    >>> uses_all('elephant','elp')
    True
    >>> uses_all('waffle','wafevr')
    False
    >>> uses_all('cjacjw ','jjcaw ')
    True
    >>> uses_all('chicken','chkn')
    True
    '''
    count = 0
    lenword = len(string)
    for let in string:
        if let in word:
            count += 1
    if count >= lenword:
        return True
    
    return False
   
            
def how_many_uses_all(reqlet):
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split(' '):
                if uses_all(line.lower(),reqlet.lower()):
                    count += 1
    print(count)
                    
            
def is_abecedarian(word):
    '''
    >>> is_abecedarian('abc')
    True
    >>> is_abecedarian('cba')
    False
    >>> is_abecedarian('envelope')
    False
    >>> is_abecedarian('abdhlp')
    True
    >>> is_abecedarian('abbbbccccdddeee')
    True
    '''

    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True
            

def count_abecedarian():
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split(' '):
                if is_abecedarian(line.strip()):
                    count += 1
        print(count)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #

