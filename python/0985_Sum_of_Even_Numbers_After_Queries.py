"""
Question Link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
Difficulty: Easy
Related Topics: Array
Solved by 09.17.2020 
Runtime: 832(ms), Memory Usage: 19.7(MB)
"""

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        def is_even(num):
            return num%2 == 0

        even_sum = 0
        for elem in A:
            even_sum += elem if is_even(elem) else 0

        result = []
        for diff, i in queries:
            A[i] += diff
            if is_even(A[i]):
                even_sum += diff if is_even(diff) else A[i]
            else:
                even_sum -= 0 if is_even(diff) else A[i] - diff
            result.append(even_sum)

        return result
