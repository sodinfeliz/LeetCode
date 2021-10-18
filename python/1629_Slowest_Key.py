"""
Question Link: https://leetcode.com/problems/slowest-key/
Difficulty: Easy
Related Topics: Array, String
Solved by 10.08.2021
Runtime: 52(ms), Memory Usage: 14.5(MB)
"""

# Runtime: 52(ms)(90.63%), Memory Usage: 14.5(MB)(54.46%)
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        sc, st = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > st or (duration == st and keysPressed[i] > sc):
                sc, st = keysPressed[i], duration
        return sc
