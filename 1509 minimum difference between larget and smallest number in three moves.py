 nums.sort()
        if len(nums) <= 4: #every number can be chnaged to be the same 
            return 0
        windowsize = len(nums) - 4 # 0 indexed hence - 3 -1
        ans = float('inf')
        for i in range (len(nums) - windowsize):
            ans = min (ans, abs(nums[i] - nums[i+windowsize]))
        return ans