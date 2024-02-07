class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_min = curr_max = nums[0]
        count = 1 

        for num in nums:
            curr_max = max(curr_max, num)
            curr_min = min(curr_min, num)

            if curr_max - curr_min > k:
                count += 1
                curr_max = curr_min = num
        return count 
            
        