"""
Question Link: https://leetcode.com/problems/goal-parser-interpretation/
Difficulty: Easy
Related Topics: String
Solved by 09.14.2021
Runtime: 40(ms), Memory Usage: 14.1(MB)
"""

class Solution:
    def interpret(self, command: str) -> str:
        if not command:
            return command
        if command[0] == 'G':
            return 'G' + self.interpret(command[1:])
        elif command[:2] == '()':
            return 'o' + self.interpret(command[2:])
        else:
            return 'al' + self.interpret(command[4:])