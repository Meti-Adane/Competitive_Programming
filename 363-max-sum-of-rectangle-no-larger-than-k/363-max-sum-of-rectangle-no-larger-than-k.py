class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        row, col = len(matrix), len(matrix[0])
        for i in range(col):
            prevSum = [0] * row
            for j in range(i, col):
                currSum = 0
                curlstSum = [0]
                for t in range(row):
                    prevSum[t] += matrix[t][j]
                    currSum += prevSum[t]
                    pos = bisect_left(curlstSum, currSum - k)
                    if pos < len(curlstSum):
                        if curlstSum[pos] == currSum - k:
                            return k
                        else:
                            ans = max(ans, currSum - curlstSum[pos])
                    insort(curlstSum, currSum)
        return ans

