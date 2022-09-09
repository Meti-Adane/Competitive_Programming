class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count = 0 
        
        properties.sort(key=lambda x:(-x[0],x[1]))
        
        maxa, maxd = properties[0]
        
        for i in range(len(properties)):
            a1,d1 = properties[i]
            if a1 < maxa and d1 < maxd:
                count += 1
            else:
                maxa, maxd = properties[i]
        return count 