# questionurl: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R, max_sum, h = 0, len(height) - 1, 0, 0
        while L < R:

            area = R - L
            if height[R] >= height[L]:
                h = height[L]
                L += 1
            else:
                h = height[R]
                R -= 1
            if h * area > max_sum:
                max_sum = h * area
        return max_sum