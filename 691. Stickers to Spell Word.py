class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        dp = [-1] * pow(2, n)
        dp[0] = 0
        for state in range(pow(2, n)):
            if dp[state] == -1:
                continue
            for sticker in stickers:
                new_state = state
                for letter in sticker:
                    for i in range(n):
                        if (new_state >> i) & 1:
                            continue
                        if target[i] == letter:
                            new_state |= 1 << i
                            break
                if dp[new_state] == -1 or dp[new_state] > dp[state] + 1:
                    dp[new_state] = dp[state] + 1
        return dp[-1]
