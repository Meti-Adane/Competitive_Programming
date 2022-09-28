class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        distances = []
        n = len(dominoes)
        prevF, dst = 'L', 0
        ans = list(dominoes)
        
        #count the distance of each '.' from the right force
        for i, char in enumerate(dominoes):
            if char != '.':
                prevF, dst = char, i
                if char == 'R':
                    distances.append(1)
                else:
                    distances.append(0)
            elif prevF == 'R':
                distances.append(i-dst)
            else:
                distances.append(n)
        
        prevF, dst = 'R', 0   
        j = n-1
        
        #form ans by comapring dst from left force and right force
        while j >= 0 :
            char = dominoes[j]
            leftForcedst = n 
            if char != '.':
                prevF, dst = char, j
            else:
                if prevF == 'L':
                    leftForcedst = dst - j
                ans[j] = self.calculateForce(distances, leftForcedst, j)
            j -= 1
        return "".join(ans)
               
    def calculateForce(self, distances, leftForcedst, idx):
            if leftForcedst == distances[idx]:
                return '.'
            if leftForcedst < distances[idx]:
                return 'L'
            return 'R'
            