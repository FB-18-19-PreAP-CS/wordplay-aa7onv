import re
def read_file():
    with open("words.txt") as tacos:
        count_the = 0
        for line in tacos:
            for word in line.strip().split(' '):
                #if word.lower == 'the':
                #if 'the' in word.lower():
                count_the +=1
                    #print(word)  
        print(count_the)

if __name__=="__main__":
    read_file()