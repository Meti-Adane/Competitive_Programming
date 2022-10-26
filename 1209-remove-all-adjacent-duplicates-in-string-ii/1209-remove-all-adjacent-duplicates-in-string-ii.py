class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            trailing = 0 
            if stack and stack[-1][0] == char:
                if stack[-1][1] + 1 == k:
                    while stack and stack[-1][0] == char:
                        stack.pop()
                    continue 
                else:
                    trailing = stack[-1][1]
            stack.append((char, trailing+1))
        
        return "".join([char for char, _ in stack])
            