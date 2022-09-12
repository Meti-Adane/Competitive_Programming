class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = score = 0 
        left, right = 0, len(tokens)-1
        tokens.sort()
        
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                ans = max(score, ans)
                left += 1
            elif score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return ans