# questionUrl: https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.root
        for char in (word):
            index = (ord(char) - ord('a'))
            if not trie.children[index]:
                trie.children[index] = Node()
            trie = trie.children[index]
        trie.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        temp = self.root
        for char in word:
            index = ord(char) - ord('a')
            temp = temp.children[index]
            if not temp:
                return False

        if temp.endOfWord == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not (temp.children[index]):
                return False
            temp = temp.children[index]
        return True