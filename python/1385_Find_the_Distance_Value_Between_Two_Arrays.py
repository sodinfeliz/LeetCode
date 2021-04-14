"""
Question Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
Difficulty: Easy
Related Topics: Array
Solved by 08.03.2020 
Runtime: 104(ms), Memory Usage: 14.1(MB)
"""

# time complexity: O(n^2), Space Complexity: O(1)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for elem1 in arr1:
            count += 1
            for elem2 in arr2:
                if abs(elem1 - elem2) <= d:
                    count -= 1
                    break
        return count
