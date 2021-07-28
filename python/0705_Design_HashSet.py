"""
Question Link: https://leetcode.com/problems/design-hashset/
Difficulty: Easy
Related Topics: Hash Table, Linked List, Array
Solved by 07.26.2021
Runtime: 1236(ms), Memory Usage: 18.7(MB)
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []

    def add(self, key: int) -> None: # O(n) 
        if key not in self.lst:
            self.lst.append(key)

    def remove(self, key: int) -> None: # O(n)
        if key in self.lst:
            del self.lst[self.lst.index(key)]

    def contains(self, key: int) -> bool: # O(n)
        """
        Returns true if this set contains the specified element
        """
        return key in self.lst

