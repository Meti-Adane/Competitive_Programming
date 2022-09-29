class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 
        for i, bar_height in enumerate(heights):
            bar_start_idx = i
            while stack and bar_height <= stack[-1][0]:
                prevheight, previdx = stack.pop()
                maxArea = max(maxArea, prevheight*(i-previdx))
                bar_start_idx = previdx # i can extend it upto the prev rectangle
            stack.append((bar_height, bar_start_idx))
        for height, pos in stack:
            maxArea = max(maxArea, height*(len(heights)-pos))
        return maxArea
                
