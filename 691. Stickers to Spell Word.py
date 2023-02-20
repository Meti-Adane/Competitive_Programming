class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = pow(2, len(target))
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] == -1:
                continue
            for sticker in stickers:
                curr = i
                for char in sticker:
                    for j in range(len(target)):
                        if (curr >> j) & 1:
                            continue
                        if target[j] == char:
                            curr |= 1 << j
                            break
                if dp[curr] == -1 or dp[curr] > dp[i] + 1:
                    dp[curr] = dp[i] + 1
        return dp[-1]