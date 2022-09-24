class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashmap = dict() #id : set(mins)
        ans = [0 for _ in range(k)]
        for userid, time in logs:
            if userid not in hashmap:
                hashmap[userid] = set()
            hashmap[userid].add(time)
        
        for user, totalmins in hashmap.items():
            ans[len(totalmins)-1] += 1
        return ans
        