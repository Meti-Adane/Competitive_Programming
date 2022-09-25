class Solution:
    def decodeString(self, s: str) -> str:
        stack, nums, opening = [], [], []
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        i = 0 
        
        while i < len(s):
            char = s[i]
            if char in digits:
                num = char
                while i+1 < len(s) and s[i+1] in digits:
                    num += s[i+1]
                    i += 1
                nums.append(int(num))
            elif char == ']':
                lastopening = opening.pop()
                prevstr = "".join(stack[lastopening:])
                stack = stack[:lastopening]
                mult = nums.pop()
                newstr = mult * prevstr
                stack.append(newstr)
            elif char == '[':
                opening.append(len(stack))
            else:
                stack.append(char)
            i += 1
        return "".join(stack)