"""
Question Link: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Related Topics: String
Solved by 07.18.2020 
Runtime: 32(ms), Memory Usage: 14(MB)
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        match_index = 0
        for i, ch in enumerate(strs[0]):
            try:
                if all([strs[index][i]==ch for index in range(1, len(strs))]):
                    match_index = i + 1
                else:
                    break
            except IndexError:
                break
        return strs[0][:match_index]