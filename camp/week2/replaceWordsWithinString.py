# question url : https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        temp = self.root
        for char in word:
            index = ord(char) - ord('a')

            if not temp.children[index]:
                temp.children[index] = TrieNode()
            temp = temp.children[index]
        temp.isEndOfWord = True

    def prefix(self, wordToSearch):
        temp = self.root
        output = ""
        for char in wordToSearch:
            index = ord(char) - ord('a')
            temp = temp.children[index]

            if not temp:
                return wordToSearch

            output += char
            if temp.isEndOfWord:
                return output
        return wordToSearch


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        trie = Trie()
        for dicti in dictionary:
            trie.insert(dicti)
        for i in range(len(words)):
            words[i] = trie.prefix(words[i])
        return ' '.join(map(str, words))
