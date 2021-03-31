"""
Question Link: https://leetcode.com/problems/jump-game/
Difficulty: Medium
Related Topics: Array, Greedy, DP
Solved by 11.04.2020 
Runtime: 76(ms), Memory Usage: 16(MB)
"""

# Time complexity: O(n), Space Complexity: O(?)
class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False

        max_step = nums[0]
        for move in nums[1:-1]:
            max_step -= 1
            if move == 0:
                if max_step > 0:
                    continue
                else:
                    return False
            else:
                max_step = max(max_step, move)

        return True
