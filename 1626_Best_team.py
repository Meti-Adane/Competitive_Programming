class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        arr = sorted(zip(ages, scores))
        ans = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):
            age1, score1 = arr[i]
            curr = ans[i] = score1

            for j in range(i+1, n):
                age2, score2 = arr[j]
                
                if age2 == age1 or score2 >= score1:
                    ans[i] = max(ans[i], curr + ans[j])
        return max(ans)
