"""
Question Link: https://leetcode.com/problems/find-common-characters/
Difficulty: Easy
Related Topics: Array, Hash Table, String
Solved by 08.26.2021 
Runtime: 44(ms), Memory Usage: 14.3(MB)
"""

# Runtime: 44(ms)(87.13%), Memory Usage: 14.3(MB)(62.6%)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        
        table = Counter(words[0])
        for word in words[1:]:
            tmp_dict = table.copy() 
            for k, v in tmp_dict.items():
                count = word.count(k)
                if count == 0:
                    del table[k]
                elif count < v:
                    table[k] = count
                    
            if len(table) == 0:
                break
            
        result = []
        for k, v in table.items():
            result += [k]*v
            
        return result
