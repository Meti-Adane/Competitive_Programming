class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        counter = Counter(arr)
        dp = [0] * len(arr)
        arr.sort()
        
        def recurse(index):
            if index < 0 or dp[index] > 0 :
                return dp[index]
            dp[index] = 1
          
            for j in range(index-1, -1, -1):
                parent, child1 = arr[index], arr[j]
                if (parent / child1) in counter:
                    child2index = arr.index(parent/child1)
                    dp[index] += (recurse(j) * recurse(child2index))
                    
            recurse(index-1)
            return dp[index]
        recurse(len(arr)-1)
        
        return sum(dp )% (10**9+7)