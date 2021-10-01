"""
Question Link: https://leetcode.com/problems/unique-morse-code-words/
Difficulty: Easy
Related Topics: Array, Hash Table, String
Solved by 09.06.2021
Runtime: 28(ms), Memory Usage: 14.2(MB)
"""

# Runtime: 28(ms)(96.38%), Memory Usage: 14.2(MB)(59.43%)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
            'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
            'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
            'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
            'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."}
        result = set()
        for word in words:
            code = ''
            for c in word:
                code += morse[c]
            result.add(code)
            
        return len(result)
