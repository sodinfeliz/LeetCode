"""
Question Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Difficulty: Easy
Related Topics: Array, Greedy
Solved by 11.02.2020 
Runtime: 56(ms), Memory Usage: 14.9(MB)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tb = 0  # local/total benefit
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff >= 0:
                tb += diff
        return tb
