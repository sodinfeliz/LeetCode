"""
Question Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Related Topics: Array, DP
Solved by 11.02.2020 
Runtime: 68(ms), Memory Usage: 15(MB)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lb = gb = 0  # local/global benefit
        for i in range(1, len(prices)):
            lb = max(0, lb+prices[i]-prices[i-1])
            gb = max(gb, lb)
        return gb
