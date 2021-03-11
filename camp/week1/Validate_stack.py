# question url : https://leetcode.com/contest/weekly-contest-112/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []

        for i in (pushed):
            pop = popped[0]
            s.append(i)
            while len(s) and pop == s[-1]:
                s.pop()
                popped.pop(0)
                if len(popped) != 0:
                    pop = popped[0]

        return len(s) == 0