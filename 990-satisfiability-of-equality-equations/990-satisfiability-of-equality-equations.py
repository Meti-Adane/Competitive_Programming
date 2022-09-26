class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leaders = [i for i in range(26)]
        
        def find(a):
            if leaders[a] == a:
                return leaders[a]
            leaders[a] = find(leaders[a])
            return leaders[a]

        def union(a, b):
            leader_of_a = find(a)
            leader_of_b = find(b)
            
            leaders[leader_of_a] = leader_of_b
            
        
        for eq in equations:
            if eq[1] == "=":                
                index1 = ord(eq[0]) - ord('a')
                index2 = ord(eq[-1]) - ord('a')
                union(index1,index2)
                
        for eq in equations:
            if eq[1] == "!":
                
                index1 = ord(eq[0]) - ord('a')
                index2 = ord(eq[-1]) - ord('a')
                if find(index1) == find(index2):
                    return False
        
        return True