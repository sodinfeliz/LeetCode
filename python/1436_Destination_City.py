"""
Question Link: https://leetcode.com/problems/destination-city/
Difficulty: Easy
Related Topics: Hash Table, String
Solved by 07.26.2021
Runtime: 44(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 44(ms)(98.69%), Memory Usage: 14.3(MB)(48.87%)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        htable = dict()
        for _from, _to in paths:
            htable[_from] = _to
            
        end = paths[0][1]
        while end in htable:
            end = htable[end]
            
        return end

# Runtime: 48(ms)(93.54%), Memory Usage: 14.3(MB)(75.93%)
# Author: YehudisK
# Thoughts:
#   Since the result must be a full path, then the 
#   starting an end point must conyain in paths only once.
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting = set([a[0] for a in paths])
        for p in paths:
            if p[1] not in starting: return p[1]
