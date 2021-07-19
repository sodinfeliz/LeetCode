"""
Question Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Difficulty: Easy
Related Topics: Array, Hash Table
Solved by 07.21.2020 
Runtime: 76(ms), Memory Usage: 13.9(MB)
"""

# time complexity: O(nlogn), Space Complexity: O(1)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_sorted = sorted(nums)
        return [num_sorted.index(i) for i in nums]
