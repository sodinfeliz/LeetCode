"""
Question Link: https://leetcode.com/problems/jewels-and-stones/
Difficulty: Easy
Related Topics: Hash Table, String
Solved by 07.23.2021
Runtime: 32(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        htable = dict()
        for s in stones:
            htable[s] = htable.get(s, 0) + 1
        
        result = 0
        for j in jewels:
            result += htable.get(j, 0)
        
        return result
