class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        hashmap = Counter(changed)
        ans = []
        changed.sort()
        
        for num in changed:
            if hashmap[num] <= 0 or num == 0 and hashmap[0] < 2:
                continue
            if num != 0 and (num * 2 not in hashmap or hashmap[num*2] <= 0):
                return []
            ans.append(num)
            hashmap[num] -=1
            hashmap[num*2] -= 1
        if len(ans) < len(changed) / 2:
            return []
        return ans