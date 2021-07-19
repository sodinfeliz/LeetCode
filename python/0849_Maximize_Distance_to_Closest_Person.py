"""
Question Link: https://leetcode.com/problems/maximize-distance-to-closest-person/
Difficulty: Medium
Related Topics: Array
Solved by 10.29.2020 
Runtime: 132(ms), Memory Usage: 14.5(MB)
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_exist = False
        cur_len = 0
        max_len = 0
        for status in seats:
            if status == 0:
                cur_len += 1
            else:
                if not left_exist:
                    left_exist = True
                    max_len = cur_len

                else:
                    max_len = max(max_len, (cur_len+1)//2)
                cur_len = 0
        return max(max_len, cur_len)
