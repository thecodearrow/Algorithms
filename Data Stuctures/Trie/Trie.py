class Trie:
    def __init__(self):
        self.letters={}
    
    def addString(self,string):
        letters=self.letters
        for c in string:
            if(c not in letters):
                letters[c]={}
            letters=letters[c]
        
        letters["*"]=True #Marks the end of a word
    
    def containsString(self,string):
        letters=self.letters
        for c in string:
            if(c not in letters):
                return False
            letters=letters[c]
        
        if("*" in letters):
            #end of string
            return True
        return False