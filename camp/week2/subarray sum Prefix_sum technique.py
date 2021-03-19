# question url: https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = count = 0
        counter = {0: 1}

        for num in nums:
            sums += num

            if counter.get(sums - k):
                count += counter.get(sums - k)

            if counter.get(sums):
                counter[sums] += 1
            else:
                counter[sums] = 1
        return count
