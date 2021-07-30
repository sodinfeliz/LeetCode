"""
Question Link: https://leetcode.com/problems/pascals-triangle-ii/
Difficulty: Easy
Related Topics: Array, DP
Solved by 07.29.2021
Runtime: 20(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 20(ms)(99.12%), Memory Usage: 14.3(MB)(20.07%)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        init = [1, 1]
        for i in range(2, rowIndex+1):
            arr = [1]*(rowIndex+1)
            for j in range(1, i):
                arr[j] = init[j] + init[j-1]
            init = arr.copy()
        return arr

# Runtime: 28(ms)(86.34%), Memory Usage: 14.2(MB)(51.13%)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        arr = [1]*2 + [0]*(rowIndex-1)
        for i in range(2, rowIndex+1):
            for j in range(i, 0, -1):
                arr[j] = arr[j] + arr[j-1]
        return arr

# Runtime: 28(ms)(86.34%), Memory Usage: 14.2(MB)(77.70%)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1] + [0]*rowIndex
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                arr[j] = arr[j] + arr[j-1]
        return arr
