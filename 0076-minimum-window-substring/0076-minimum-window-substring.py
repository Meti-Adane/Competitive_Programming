class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ''
        
        counter = Counter(t)
        required = len(counter)
        accumulated = 0 
        hashmap = dict()
        start, end = 0, len(s)+1
        left, right = 0 , 0
        
        while right < len(s):
            char = s[right]
            if char in counter:
                hashmap[char] = hashmap.get(char, 0) + 1
                if hashmap[char] == counter[char]:
                    accumulated += 1
            
            while left <= right and accumulated >= required:
                if right-left < end-start:
                    start, end = left, right
                leftchar = s[left]
                
                if leftchar in hashmap: 
                    hashmap[leftchar] -= 1
                    if hashmap[leftchar] < counter[leftchar]:
                        accumulated -= 1
                left += 1
                
            right += 1
        return s[start:end+1] if end < len(s)+1 else ''
                
                    
                
                
            
            
       


        
        
        