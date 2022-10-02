class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        curr_prod = 1
        
        for val in nums:
            curr_prod *= val
            ans.append(curr_prod)
            
        curr_prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i-1] * curr_prod if i - 1 >= 0 else curr_prod
            curr_prod *= nums[i]
        return ans 