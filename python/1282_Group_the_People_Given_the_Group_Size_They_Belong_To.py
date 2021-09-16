"""
Question Link: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
Difficulty: Medium
Related Topics: Array, Hash Table
Solved by 09.07.2020
Runtime: 76(ms), Memory Usage: 14.6(MB)
"""

# Runtime: 76(ms)(74.42%), Memory Usage: 14.6(MB)(14.46%)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        arr = []
        for idx, gs in enumerate(groupSizes):
            arr.append((gs, idx))
        arr.sort()
        ptr, result = 0, []
        while ptr < len(groupSizes):
            result.append([elem[1] for elem in arr[ptr: ptr+arr[ptr][0]]])
            ptr += arr[ptr][0]
        return result

# Author: @lee215
# Runtime: 72(ms)(90.60%), Memory Usage: 14.3(MB)(73.81%)
class Solution:
	def groupThePeople(self, groupSizes):
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in xrange(0, len(l), s)]
