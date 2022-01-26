"""
Question Link: https://leetcode.com/problems/design-circular-queue/
Difficulty: Medium
Related Topics: Array, Linked List, Queue, Design
Solved by 01.14.2022
Runtime: 76(ms), Memory Usage: 14.9(MB)
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.head = 0
        self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.queue[self.tail] = value
        else:
            self.tail = (self.tail + 1) % len(self.queue)
            self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.head] = None
        if self.head != self.tail:
            self.head = (self.head + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        value = self.queue[self.head]
        return -1 if value is None else value

    def Rear(self) -> int:
        value = self.queue[self.tail]
        return -1 if value is None else value

    def isEmpty(self) -> bool:
        return self.queue[self.head] is None

    def isFull(self) -> bool:
        return (self.tail + 1) % len(self.queue) == self.head and \
            self.queue[self.head] is not None and \
            self.queue[self.tail] is not None
