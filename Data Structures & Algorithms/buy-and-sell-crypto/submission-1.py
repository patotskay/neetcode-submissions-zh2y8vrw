class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        ans = 0
        for r in range(1, n):
            if prices[r] < prices[l]:
                l = r 
            if prices[r] > prices[l]:
                ans = max(ans, prices[r] - prices[l])
        return ans

