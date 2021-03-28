file=open("C:/Users/yarde/Dropbox/My PC (LAPTOP-3RT6OQVU)/Desktop/pythonprogram/2/test.txt")
def revword (word:str):
    new_word=word[::-1]
    new_word=new_word.lower()
    return new_word

def countword (file):
    for line in file:
        line = line.strip("\n")
        word=line
        break
    
    counter=1
    for line in file:
        line = line.strip("\n")
        if line==word: continue
        words=line.split()
        for i in words:
            revword(i)
            if revword(i)==word:
                counter+=1
    return counter 