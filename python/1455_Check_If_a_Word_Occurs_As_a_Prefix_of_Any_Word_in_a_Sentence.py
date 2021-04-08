"""
Question Link: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
Difficulty: Easy
Related Topics: String
Solved by 11.03.2020 
Runtime: 28(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.strip()
        index, skip = 0, 0
        find = False
        while index < len(sentence):
            if sentence[index: index+len(searchWord)] == searchWord:
                find = True
                break
            else: # skip the spaces
                while index < len(sentence) and sentence[index] != ' ':
                    index += 1
                while index < len(sentence) and sentence[index] == ' ':
                    index += 1
                skip += 1

        if find:
            return skip + 1
        else:
            return -1
