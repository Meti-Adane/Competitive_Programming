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
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = TrieNode(char)
            temp = temp.children[char]
        temp.isEnd = True
    def recurse(self, curr, word, node):

        if curr == '.':
            for i in range(ord('a'), ord('z') +1):
                char = chr(i)
                if char in node.children and self.recurse(char, word, node):
                    return True 
            return False 
        
        else:
            if curr not in node.children:
                return False
            # If there are more charachters to match continue the check 
            # If this is the last character check if the node is indicates end 
            return ((word and self.recurse(word[0], word[1:], node.children[curr])) or 
                         (not word and node.children[curr].isEnd))
      
                
   
    def search(self, word: str) -> bool:
        return self.recurse(word[0], word[1:], self.root)
        
        
        


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