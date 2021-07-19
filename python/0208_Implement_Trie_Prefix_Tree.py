"""
Question Link: https://leetcode.com/problems/implement-trie-prefix-tree/
Difficulty: Medium
Related Topics: Design, Trie
Solved by 11.03.2020 
Runtime: 216(ms), Memory Usage: 31.3(MB)
"""

# Reference from pn07
class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isCompleted = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch, TrieNode())
            currNode.childNodes[ch] = node
            currNode = node
            
        currNode.isCompleted = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        find = True
        currNode = self.root
        for ch in word:
            if ch not in currNode.childNodes:
                return False
            else:
                 currNode = currNode.childNodes[ch]            
        return currNode.isCompleted

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        find = True
        currNode = self.root
        for ch in prefix:
            if ch not in currNode.childNodes:
                return False
            else:
                 currNode = currNode.childNodes[ch]                    
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)