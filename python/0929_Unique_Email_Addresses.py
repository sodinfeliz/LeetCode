"""
Question Link: https://leetcode.com/problems/unique-email-addresses/
Difficulty: Easy
Related Topics: Array, Hash Table, String
Solved by 09.06.2021
Runtime: 40(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 40(ms)(98.9%), Memory Usage: 14.3(MB)(60.72%)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            local, *_ = local.split('+', 1)
            result.add(f'{local}@{domain}')
        return len(result)
