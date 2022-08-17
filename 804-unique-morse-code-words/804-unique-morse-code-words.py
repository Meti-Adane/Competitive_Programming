#8:34
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        
        
        for pos, word in enumerate(words):
            transformation = []
            for char in word:
                transformation.append(morse_code[ord(char)%97])
            ans.add("".join(transformation))
            
        return len(ans)