"""
Question Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy
Related Topics: Array, Binary Search
Solved by 01.24.2021
Runtime: 261(ms), Memory Usage: 15.6(MB)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        find_index = None
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                find_index = mid
                break
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
            
        return -1 if find_index is None else find_index
