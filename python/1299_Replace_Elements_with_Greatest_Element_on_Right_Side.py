"""
Question Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Difficulty: Easy
Related Topics: Array
Solved by 07.15.2020 
Runtime: 128(ms), Memory Usage: 15.1(MB)
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        arr = arr[1:]
        arr.append(-1)
        max_val = arr[-2]
        for index in range(len(arr)-3, -1, -1):
            if arr[index] <= max_val:
                arr[index] = max_val
            else:
                max_val = arr[index]
        return arr
