class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = Counter(arr)
        self.ans = 0 
        arr.sort()
        
        def recurse(index):
            if index >= len(arr):
                return 0
            parent = arr[index]
            for j in range(index):
                child1 = arr[j]
                child2 = parent /child1
                if child2 in dp:
                    dp[parent] += dp[child1] * dp[child2]
                    
            recurse(index+1)
            self.ans += dp[parent]
            return dp[parent]
        
        recurse(0)
        return self.ans% (10**9+7)