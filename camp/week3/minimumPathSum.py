# question url : https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = dict()
        return self.traveseNew(triangle, 0, 0, memo)

    def traveseNew(self, triangle, row, col, memo):
        if memo.get((row, col)):
            return memo[(row ,col)]

        if row == len(triangle) - 1:
            return triangle[row][col]

        memo[(row, col)] = min(self.traveseNew(triangle, row +1, col, memo), self.traveseNew(triangle, row +1, col +1, memo)) + triangle[row][col]

        return memo[(row ,col)]