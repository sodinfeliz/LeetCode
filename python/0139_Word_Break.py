"""
Question Link: https://leetcode.com/problems/word-break/
Difficulty: Medium
Related Topics: Hash Table, String, DP, Memoization, Trie 
Solved by 09.10.2021 
Runtime: 46(ms), Memory Usage: 14.4(MB)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        flag = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if not flag[j]:
                    continue
                if s[j:i] in wordDict:
                    flag[i] = True
                    break
        return flag[-1]
