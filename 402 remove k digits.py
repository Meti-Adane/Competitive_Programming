class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k == len(num):
            return "0"
        
        for pos, digit in enumerate(num):
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            if stack or digit != '0':
                stack.append(digit)
        
        if k:
            stack = stack[:len(stack)-k]

        if not stack:
            return '0'
        return "".join(stack)
