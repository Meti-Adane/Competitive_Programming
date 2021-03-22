# questionurl : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = None
        for i in range(len(prices) - 1):
            if curr == None and (prices[i + 1] > prices[i]):
                curr = prices[i]
            elif curr != None and (prices[i + 1] < prices[i]):
                profit += prices[i] - curr
                curr = None

        if curr != None:
            profit += prices[i + 1] - curr
            curr = None

        return profit