"""
Question Link: https://leetcode.com/problems/count-and-say/
Difficulty: Easy
Related Topics: String
Solved by 11.03.2020 
Runtime: 32(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        currStr = '1'
        for i in range(1, n):
            nextStr = ''
            currCh, nCh = currStr[0], 1
            for ch in currStr[1:]:
                if ch == currCh:
                    nCh += 1
                else:
                    nextStr += f'{nCh}{currCh}' 
                    currCh = ch
                    nCh = 1
            currStr = nextStr + f'{nCh}{currCh}' 
        return currStr