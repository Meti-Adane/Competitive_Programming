class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #(temp, index)
        ans = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prevtemp, idx = stack.pop()
                ans[idx] =  i - idx
            stack.append((temp, i))
        return ans
