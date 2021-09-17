"""
Question Link: https://leetcode.com/problems/jewels-and-stones/
Difficulty: Medium
Related Topics: Hash Table, Math
Solved by 09.07.2021
Runtime: 40(ms), Memory Usage: 14.4(MB)
"""

# Runtime: 40(ms)(82.96%), Memory Usage: 14.4(MB)(63.99%)
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.defaultdict(int)
        for idx, ans in enumerate(answers):
            count[ans+1] += 1
        total = 0
        for k, v in count.items():
            total += (v//k + 1*(v%k >0))*k
        return total
