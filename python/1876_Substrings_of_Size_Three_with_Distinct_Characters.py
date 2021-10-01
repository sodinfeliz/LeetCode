"""
Question Link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
Difficulty: Easy
Related Topics: Hash Table, String, Counting
Solved by 09.30.2021
Runtime: 32(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 32(ms)(78.24%), Memory Usage: 14.2(MB)(70.31%)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            if self.is_good_substring(s[i: i+3]):
                count += 1
        return count
    
    def is_good_substring(self, sub: str) -> bool:
        assert len(sub) == 3
        return sub[0] != sub[1] and sub[0] != sub[2] and sub[1] != sub[2]


# Reference Code
# Author: @sethhritik
#   Using set instead of character comparisons.
def countGoodSubstrings(self, s: str) -> int:
    ans=0
    for i in range(len(s)-2):
        if len(set(s[i:i+3]))==3:
            ans+=1
    return ans
