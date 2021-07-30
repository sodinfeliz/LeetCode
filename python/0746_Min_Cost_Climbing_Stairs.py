"""
Question Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Difficulty: Easy
Related Topics: Array, DP
Solved by 07.29.2021
Runtime: 60(ms), Memory Usage: 14.3(MB)
"""

# Time complexity: O(n), Space Complexity: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = [0]*(len(cost)-2) + cost[-2:]
        for i in range(len(total_cost)-3, -1, -1):
            total_cost[i] = cost[i] + min(total_cost[i+1], total_cost[i+2])
        return min(total_cost[0], total_cost[1])

# Time complexity: O(n), Space Complexity: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            cost[i] += cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
