class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        counter = Counter(arr)
        dp = [0] * len(arr)
        self.ans = 0 
        arr.sort()
        
        def recurse(index):
            if index >= len(arr):
                return 0
            if dp[index] > 0 :
                return dp[index]
            dp[index] = 1
            
            for j in range(index):
                parent, child1 = arr[index], arr[j]
                if (parent / child1) in counter:
                    child2index = arr.index(parent/child1)
                    dp[index] += (recurse(j) * recurse(child2index))
                    
            recurse(index+1)
            self.ans += dp[index]
            return dp[index]
        
        recurse(0)
        return self.ans% (10**9+7)