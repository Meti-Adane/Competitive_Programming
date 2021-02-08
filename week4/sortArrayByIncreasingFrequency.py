# question url: https://leetcode.com/problems/sort-array-by-increasing-frequency
class Solution:
    def frequencySort(self, nums):
        nums.sort()
        nums.reverse()
        frequency = {}
        sorted_list = []
        for i in nums:
            count = 0
            fast = len(nums) - 1
            slow = 0
            while (fast >= slow):
                if fast != slow and i == nums[fast] and i == nums[slow]:
                    count += 2
                elif i == nums[fast] or i == nums[slow]:
                    count += 1

                fast -= 1
                slow += 1
            frequency[i] = count

        s = sorted(frequency.keys(), key=lambda k: frequency[k])
        for j in s:
            for r in range(frequency[j]):
                sorted_list.append(j)
        return sorted_list