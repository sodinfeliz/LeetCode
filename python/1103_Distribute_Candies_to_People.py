"""
Question Link: https://leetcode.com/problems/distribute-candies-to-people/
Difficulty: Easy
Related Topics: Math
Solved by 10.31.2020 
Runtime: 48(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist = [0] * num_people
        dn, idx = 1, 0
        while candies > 0:
            dist[idx % num_people] += min(dn, candies)
            candies -= dn
            dn += 1
            idx += 1
        return dist
