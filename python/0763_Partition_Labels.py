"""
Question Link: https://leetcode.com/problems/partition-labels/
Difficulty: Medium
Related Topics: Hash Table, Two Pointers, String, Greedy
Solved by 09.14.2021
Runtime: 54(ms), Memory Usage: 14.1(MB)
"""

# Runtime: 54(ms)(23.78%), Memory Usage: 14.1(MB)(93.71%)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_range = dict()
        for i, ch in enumerate(s):
            if ch not in letter_range:
                letter_range[ch] = [i, i]
            else:
                letter_range[ch][1] = i
        
        mutual = []
        for r in letter_range.values():
            if mutual:
                if r[1] < mutual[-1][1]:
                    continue
                elif r[0] > mutual[-1][1]:
                    mutual.append(r)
                else:
                    mutual[-1][1] = r[1]
            else:
                mutual.append(r)
         
        return [interv[1] - interv[0] + 1 for interv in mutual]
