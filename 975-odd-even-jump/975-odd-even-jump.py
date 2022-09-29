class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n, ans = len(arr), 1
        next_higher = [-1 for i in range(len(arr))]
        next_lower = [-1 for i in range(len(arr))]
        sorted_index = sorted([i for i in range(len(arr))], key=lambda x:[arr[x]])
        
        stack = []
        for i in range(len(sorted_index)):
            idx = sorted_index[i]
            while stack and idx > stack[-1]:
                next_higher[stack.pop()] = idx
            stack.append(idx)
        
        sorted_index.sort(key=lambda x:[arr[x], -1*x]) #this was the weirdest part that took time but essentially for the next lower element i want to get the element with smaller index but incase of equal elements i want the smaller index so i had to reverse the indicies for equivalent values gn demo lemejemriyaw this doesnt work so it needs to be placed here
        stack = []
        for i in range(len(arr)-1, -1, -1):
            idx = sorted_index[i]
            while stack and idx > stack[-1]:
                next_lower[stack.pop()] = idx
            stack.append(idx)
            
        jumps = [(0, 0) for i in range(len(arr))]
        jumps[-1] = (1, 1) #odd,even | hasnextvalidhighervalue,hasvalidnextlowervalue
        
        for i in range(len(arr)-2, -1, -1): #-2 bc lastindex has been pre processed 
            hasnexthigher, hasnextlower = 0, 0
            if next_higher[i] >-1:
                hasnexthigher = jumps[next_higher[i]][1]
            if next_lower[i] > -1:
                hasnextlower = jumps[next_lower[i]][0]
            if hasnexthigher:
                ans += 1
            jumps[i] = (hasnexthigher, hasnextlower)
        return ans
            
        