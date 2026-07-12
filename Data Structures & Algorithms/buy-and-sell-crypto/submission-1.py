class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r <= len(prices) - 1:
            if prices[r] - prices[l] > res:
                res = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l += 1
                if l == r:
                    r += 1
            
            else:
                r += 1

        return res