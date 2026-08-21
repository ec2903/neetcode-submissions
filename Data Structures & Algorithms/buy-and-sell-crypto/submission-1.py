class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0] #assume that the earliest date is the cheapest

        for price in prices:
             maxProfit = max(maxProfit, price - minBuy) #compares maxProfit with current price - lowest price
             minBuy = min(minBuy, price)
        
        return maxProfit



        