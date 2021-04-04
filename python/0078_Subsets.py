"""
Question Link: https://leetcode.com/problems/subsets/
Difficulty: Medium
Related Topics: Array
Solved by 10.23.2020 
Runtime: 36(ms), Memory Usage: 14.3(MB)
"""

class Solution:
    def subsets(self, nums):
        lnum = len(nums)
        all_subset = []
        for i in range(2**lnum):
            bnum = bin(i)[2:]
            bnum = '0'*(lnum - len(bnum)) + bnum
            states = list(map(int, bnum))
            subset = [nums[idx] for idx, state in enumerate(states) if state==1]
            all_subset.append(subset)
        return all_subset
