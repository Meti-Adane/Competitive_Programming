class Solution:
    def reverseWords(self, s: str) -> str:
        length = []
        chars = list(s)
        j = 0
        
        while j < len(s):
            i = j
            while i < len(s) and s[i] != " ":
                i += 1
            length.append((j, i))
            j = i +1
            
        for start, end in length:
            end -= 1
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        return "".join(chars)
