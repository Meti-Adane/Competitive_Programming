# question url : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in range(len(grid)):
            right = len(grid[0]) - 1
            left = 0
            while left <= right and grid[row][left] >= 0:
                mid = (right + left) // 2
                if grid[row][mid] < 0:
                    right = mid
                elif grid[row][mid] >= 0:
                    left = mid + 1
            count += len(grid[0]) - left
        return count