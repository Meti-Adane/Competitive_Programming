# questionurl : https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forwardsums = backwardsums = [0]
        backwardspointer = len(nums) - 1

        for i in range(len(nums) - 1):
            forwardsums.append(nums[i] + forwardsums[i])
            backwardsums.append(nums[backwardspointer] + backwardsums[i])
            backwardspointer -= 1

        backwardsums.reverse()

        for i in range(len(backwardsums)):
            if backwardsums[i] == forwardsums[i]:
                return i
        return -1