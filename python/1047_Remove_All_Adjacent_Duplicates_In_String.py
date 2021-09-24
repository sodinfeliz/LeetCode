"""
Question Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Difficulty: Easy
Related Topics: String, Stack
Solved by 09.13.2021 
Runtime: 956(ms), Memory Usage: 15.6(MB)
"""

# Time complexity: O(n^2), Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        for i, ch in enumerate(s[:-1]):
            if ch == s[i+1]:
                j = i
                while j != 0:
                    if s[j-1: i+1] == s[i+1: i+(i-j)+3][::-1]:
                        j -= 1
                    else:
                        break
                s = s.replace(f'{s[j:i+1]}{s[j:i+1][::-1]}', '')
                return self.removeDuplicates(s)
        return s

# Reference Code
# Runtime: 72(ms)(92.33%), Memory Usage: 15.3(MB)(38.03%)
# Time complexity: O(n), Space Complexity: O(n)
# Most voted post, Author: @lee215
class Solution:
    def removeDuplicates(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
