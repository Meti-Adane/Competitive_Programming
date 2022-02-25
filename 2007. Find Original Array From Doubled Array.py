class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        hashmap = Counter(changed)
        ans = []
        changed.sort()
        # if len(changed) %2 != 0:
        #     return []
        for num in changed:
            if hashmap[num] == 0:
                continue
            hashmap[num] -= 1
            target = num * 2
            if target in hashmap and hashmap[target] > 0 : 
                ans.append(num)
                hashmap[target] -= 1
        
        
        return ans if len(ans) == math.ceil(len(changed) / 2) else []
    
    
  