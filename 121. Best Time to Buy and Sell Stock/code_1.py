class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy + 1
            
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
        return profit

# O(n) time complexity, O(1) space complexity