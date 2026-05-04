class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            minPrice = min(price,minPrice)
            profit = price-minPrice
            maxProfit = max(profit,maxProfit)
        return maxProfit