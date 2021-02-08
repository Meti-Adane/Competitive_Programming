# question url : https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        sums = [0,1,1]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        for i in range(2, n):
            sums.append(sum(sums[i-2:]))
        return sums[-1]