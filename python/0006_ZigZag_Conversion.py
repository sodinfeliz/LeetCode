"""
Question Link: https://leetcode.com/problems/zigzag-conversion/
Related Topics: String
Solved by 11.04.2020 
Runtime: 44(ms), Memory Usage: 14.2(MB)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]

        rowStr = ['']*numRows
        segLen = 2*numRows - 2

        for idx in range(0, len(s), segLen):
            seg = s[idx: idx + segLen].ljust(segLen)
            for i in range(numRows):
                if i in [0, numRows-1]:
                    rowStr[i] += seg[i]
                else:
                    rowStr[i] += seg[i] + seg[-i]

        rowStr = list(map(str.rstrip, rowStr))
        return ''.join(rowStr)