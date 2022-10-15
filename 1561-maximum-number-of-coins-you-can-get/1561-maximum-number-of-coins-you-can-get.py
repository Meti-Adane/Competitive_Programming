class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        picker, ans, bob = len(piles)-2, 0, 0
        while picker >= bob:
            ans += piles[picker]
            picker -= 2
            bob += 1
        return ans 