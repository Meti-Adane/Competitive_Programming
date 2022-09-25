class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        op= deque()
        digits = {"0", "1", "2","3" ,"4" ,"5" ,"6" ,"7", "8","9"}
        operations = {"+", "-", "*", "/"}
        i = 0
        while i < len(s):
            if s[i] in digits:
                num = s[i]
                while i+1 < len(s) and s[i+1] in digits:
                    num += s[i+1]
                    i += 1
                
                if op and (op[-1] == '*' or op[-1] =='/'):
                    
                    val1 = stack.pop()
                    if op[-1] == "*": 
                        stack.append(val1 * int(num))
                    else:
                        stack.append(val1 // int(num))
                    op.pop()
                else:
                    stack.append(int(num))
            elif s[i] in operations:
                op.append(s[i])
            i += 1
        while op:
            operation = op.popleft()
            val1 = stack.popleft()
            val2 = stack.popleft()
            if operation == "+":
                
                stack.appendleft(val2+val1)
            else:
                stack.appendleft(val1-val2)
        return stack[0]