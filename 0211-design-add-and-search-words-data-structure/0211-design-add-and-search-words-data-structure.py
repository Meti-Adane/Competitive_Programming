'''
        "" : { ba , bo 
            b : {
             a : {
               d: {
                a : {
                  s : {
                    s: {
                    
                    }
                  }
                }
               }
             }
             o : {
              b : {
              
              }
             }
            }
        }
        
        

'''




class TrieNode:
    def __init__(self, char="", isEnd= False):
        #self.char = char # not really needed I just used it print lemadreg and debug 
        self.children = dict()
        self.isEnd = isEnd   
    
class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        if len(word) not in self.root:
            self.root[len(word)] = set()
        self.root[len(word)].add(word)
      
   
    def search(self, word: str) -> bool:
        n = len(word)
        if n not in self.root:
            return False 
        
        if '.' in word:
            for w in self.root[n]:
                res = True
                for i in range(n):
                    if word[i] != '.' and word[i] != w[i]: 
                        res = False 
                        break
                if res: return True 
        return word in self.root[n]
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
'''
      


TireNode:
    char
    children = # Trienodes 26 
    isEnd 
    

'''