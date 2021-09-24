"""
Question Link: https://leetcode.com/problems/sort-characters-by-frequency/
Difficulty: Medium
Related Topics: Hash Table, String, Heap
Solved by 09.15.2021
Runtime: 36(ms), Memory Usage: 15.6(MB)
"""

# Runtime: 36(ms)(91.01%), Memory Usage: 15.6(MB)(39.79%)
class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        count = sorted(list(count.items()), key=lambda i: i[1], reverse=True)
        return ''.join([k*v for k, v in count])
