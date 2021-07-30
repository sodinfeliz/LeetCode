"""
Question Link: https://leetcode.com/problems/counting-bits/
Difficulty: Easy
Related Topics: DP, Bit Manipulation
Solved by 07.29.2021
Runtime: 76(ms), Memory Usage: 20.9(MB)
"""

# Time complexity: O(n), Space Complexity: O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0, 1]
        if n < 2: return arr[:n+1]
        for i in range(2, n+1):
            if i % 2 == 0:
                arr.append(arr[i//2])
            else:
                arr.append(arr[i//2]+1)
        return arr
