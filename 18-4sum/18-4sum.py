class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            num1 = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                if j > i+1 and nums[j] == nums[j-1]:
                    continue 
                left, right = j+1, len(nums)-1
                newtarget = target - (num1+num2)
                while left < right:
                    if left > j+1 and nums[left] == nums[left-1]:
                        left += 1
                        continue 
                    if nums[left] + nums[right] > newtarget:
                        right -= 1
                    elif nums[left] + nums[right] < newtarget:
                        left += 1
                    else:
                        res.append([num1, num2, nums[left], nums[right]])
                        left += 1
                        right -= 1
        return res