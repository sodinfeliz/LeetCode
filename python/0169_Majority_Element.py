"""
Question Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Related Topics: Easy, D&C, Bit Manipulation
Solved by 07.17.2020 
Runtime: 216(ms), Memory Usage: 15.3(MB)
"""

# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            else:
                count += 1 if candidate == num else -1
        return candidate

# 1 Sorting : Since the assumption is that the majority element 
# always exist in the array, hence the median of the list must be 
# the majority element of nums.  But list.sort() using @Timsort 
# as the sort algorithm which have a time complexity of O(nlogn). 
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        index = len(nums) // 2  
        return nums[index]

# 2 HashMap  
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
