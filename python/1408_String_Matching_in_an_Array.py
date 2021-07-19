"""
Question Link: https://leetcode.com/problems/string-matching-in-an-array/
Difficulty: Easy
Related Topics: String
Solved by 10.29.2020 
Runtime: 36(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for w1 in words:
            for w2 in words:
                if w1 != w2 and w1 in w2:
                    result.append(w1)
                    break
        return result
