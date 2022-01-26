"""
Question Link: https://leetcode.com/problems/perfect-squares/
Difficulty: Medium
Related Topics: Math, DP, BFS
Solved by 01.25.2022
Runtime: 1292(ms), Memory Usage: 199.2(MB)
"""

# Runtime: 7604(ms)(5.01%), Memory Usage: 14.2(MB)(85.89%)
from queue import SimpleQueue


class Solution:
    def numSquares(self, n: int) -> int:
        comp, start = [], int(n**.5)
        min_len = n
  
        while True:
            comp.append(start**2)
            
            if comp[0] == 1 or start < 1:
                break
                
            if sum(comp) == n:
                if len(comp) < min_len:
                    min_len = len(comp)
                while comp[-1] == 1: 
                    comp.pop()
                start = int(comp.pop()**.5) - 1  
            elif sum(comp) > n:
                comp.pop()
                if start <= 1:
                    start = int(comp.pop()**.5) - 1
                else:
                    start -= 1
                    
            if len(comp) + 1 > min_len:
                while comp[-1] == 1: 
                    comp.pop()
                start = int(comp.pop()**.5) - 1  
                            
        return min_len


# Time Limit Exceeded
# Dynamic Programming Method (bottom-up)
class Solution:
	def numSquares2(self, n: int) -> int:
        dp = list(range(n+1))
        for i in range(2, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]


# Runtime: 1292(ms)(69.33%), Memory Usage: 199.2(MB)(5.01%)
# Breath-first Search
from queue import SimpleQueue

class Solution:
    def numSquares(self, n: int) -> int:
        
        def is_square(num: int):
            return int(num**.5)**2 == num
        
        q = SimpleQueue()        
        q.put(n)
        step = 1
        
        while not q.empty():
            sz = q.qsize()
            for _ in range(sz):
                value = q.get()
                
                if is_square(value):
                    return step
                for i in range(1, int(value**.5)+1):
                    if value - i*i > 0:
                        q.put(value - i*i)
            step += 1 
                
        return step
