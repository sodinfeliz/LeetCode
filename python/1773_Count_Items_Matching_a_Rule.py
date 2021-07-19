"""
Question Link: https://leetcode.com/problems/count-items-matching-a-rule/
Difficulty: Easy
Related Topics: Array
Solved by 03.12.2021
Runtime: 228(ms), Memory Usage: 20.7(MB)
"""

class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        key = {"type": 0, "color": 1, "name": 2}
        return len([item for item in items if item[key[ruleKey]] == ruleValue])
