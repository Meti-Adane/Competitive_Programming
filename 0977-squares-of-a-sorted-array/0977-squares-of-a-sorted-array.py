class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        ans = deque()
        while left <= right:
            x, y = pow(nums[right], 2), pow(nums[left], 2)
            if left == right:
                ans.appendleft(x)
                break
            if x >= y:
                ans.appendleft(x)
                right -= 1
            if y >= x:
                ans.appendleft(y)
                left += 1
        return ans