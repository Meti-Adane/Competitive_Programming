class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0 
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            maxFreq = max(maxFreq, counter[num])
        return sum(value for value in counter.values() if value == maxFreq)