
def at_least(): 
    with open("words.txt") as file:
        count_char = 0
        for line in file:
            for word in line.strip().split(' '):
                if len(word) >= 20:
                    count_char += 1
        print(count_char)
                
def has_no_e(word):
    with open("words.txt") as file:
        count_no_e = 0
        for line in file:
            for word in line.strip().split(' '):
                if 'e' not in word.lower():
                    return True
                
def no_e(): 
    with open("words.txt") as file:
        count_no_e = 0
        for line in file:
                for word in line.strip().split(' '):
                    if 'e' not in word.lower():
                        count_no_e += 1
    
    with open("words.txt") as file:
        num_words = 0
        for line in file:
            for word in line.strip().split(' '):
                num_words += 1
        print(count_no_e / num_words)
    
                
                    
    
                    

def avoids():
    pass
def count_avoids():
    pass

def uses_only(): 
    pass

def uses_all():
    pass

def how_many_uses_all():
    pass

def is_abecedarian():
    pass

no_e()