class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        min_price = prices[0]
        proft_current=0
        for current in prices:
            if current<=min_price:
                min_price=current
            profit_current = current-min_price
            if profit_current>=profit_max:
                profit_max=profit_current
        return profit_max