"""
Question Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Difficulty: Medium
Related Topics: Array, Hash Table, Two Pointers, Sorting
Solved by 09.08.2021
Runtime: 64(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 64(ms)(28.66%), Memory Usage: 14.4(MB)(70.83%)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                del nums2[nums2.index(num)]
        return result

# Runtime: 85(ms), Memory Usage: 14.4(MB)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                result.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
        return result
