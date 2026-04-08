class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit_curr = 0
        profit_max = 0
        for price in prices:
            min_price = min(min_price,price)
            profit_curr = price-min_price
            profit_max = max(profit_curr,profit_max)
        return profit_max