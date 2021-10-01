"""
Question Link: https://leetcode.com/problems/uncommon-words-from-two-sentences/
Difficulty: Easy
Related Topics: Hash Table, String
Solved by 09.10.2021
Runtime: 32(ms), Memory Usage: 14.2(MB)
"""
import collections

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = collections.Counter(s1.split(' '))
        for word in s2.split(' '):
            count[word] = count.get(word, 0) + 1
        return [k for k, v in count.items() if v == 1]
