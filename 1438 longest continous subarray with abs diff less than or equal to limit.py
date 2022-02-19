class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxque, minque = deque(), deque()
        right, left = 0, 0
        ans = float('-inf')
        while right < len(nums):
            num = nums[right]

            while minque and minque[-1] > num:
                minque.pop()
            minque.append(num)
            
            while maxque and maxque[-1] < num:
                maxque.pop()
            maxque.append(num)
            
            if maxque[0] - minque[0] <= limit:
                ans = max(ans, right-left+1)
            else:
                if nums[left] == maxque[0]:
                    maxque.popleft()
                if nums[left] == minque[0]:
                    minque.popleft()
                left += 1
            right += 1 
        return ans
        
        