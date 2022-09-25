class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = []
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
                que = deque()
                while stack and stack[-1] != '[':
                    que.appendleft(stack.pop())
                if stack and stack[-1] == '[':
                    stack.pop()
                if nums:
                    mult = nums.pop()
                newstr = mult * "".join(que)
                stack.append(newstr)
            else:
                stack.append(char)
            i += 1
        return "".join(stack)