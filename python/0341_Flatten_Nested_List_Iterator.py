"""
Question Link: https://leetcode.com/problems/flatten-nested-list-iterator/
Difficulty: Medium
Related Topics: Stack, Design
Solved by 04.14.2021
Runtime: 72(ms), Memory Usage: 17.8(MB)
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
    
    def next(self) -> int:
        return self.value
        
    def hasNext(self) -> bool:
        self.value = None
        while len(self.nestedList) != 0:
            head = self.nestedList[0]
            if head.isInteger():
                self.value = head.getInteger()
                self.nestedList = self.nestedList[1:]
                break
            self.nestedList = head.getList() + self.nestedList[1:]
            
        return self.value is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
