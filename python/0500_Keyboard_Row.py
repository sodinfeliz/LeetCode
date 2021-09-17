"""
Question Link: https://leetcode.com/problems/keyboard-row/
Difficulty: Easy
Related Topics: Array, Hash Table, String
Solved by 08.25.2021
Runtime: 24(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 24(ms)(95.45%), Memory Usage: 14.3(MB)(49.74%)
class Solution:
    
    htable = {
        1: 'qwertyuiop',
        2: 'asdfghjkl',
        3: 'zxcvbnm'
    }
    
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            examine = self.findCategory(word)
            in_one_row = True
            for ch in word[1:]:
                if ch.lower() not in self.htable[examine]:
                    in_one_row = False
                    break
            if in_one_row:
                result.append(word)
        return result
        
    def findCategory(self, word):
        ch = word[0].lower()
        if ch in self.htable[1]:
            return 1
        elif ch in self.htable[2]:
            return 2
        else: return 3
