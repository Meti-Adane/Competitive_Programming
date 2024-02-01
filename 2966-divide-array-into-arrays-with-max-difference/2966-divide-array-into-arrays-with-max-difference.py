class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(2, len(nums), 3):
            a, b, c = nums[i-2], nums[i-1], nums[i]
            if (c-a) > k: return []
            ans.append([a, b, c])
        return ans 

            



