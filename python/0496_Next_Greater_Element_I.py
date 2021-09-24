"""
Question Link: https://leetcode.com/problems/next-greater-element-i/
Difficulty: Easy
Related Topics: Array, Hash Table, Stack
Solved by 09.06.2020 
Runtime: 44(ms), Memory Usage: 14.6(MB)
"""

# Runtime: 44(ms)(89.11%), Memory Usage: 14.6(MB)(43.58%)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []
        
        htable = dict()
        htable[nums2[-1]] = -1
        stack, nums2 = [nums2[-1]], nums2[:-1]
        for num in nums2[::-1]:
            while stack:
                if stack[-1] > num:
                    htable[num] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack:
                htable[num] = -1
            stack.append(num)
                
        return [htable[num] for num in nums1]
