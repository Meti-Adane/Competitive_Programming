# question url : https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = float('inf')

        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ""

        self.insertWord(strs[0])
        for i in range(1, len(strs)):
            existingChars = self.insertWord(strs[i])
            minlen = min(minlen, existingChars)
        return strs[0][:minlen]

    def insertWord(self, word):
        exisitingchars = 0
        temp = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not temp.children[index]:
                temp.children[index] = TrieNode()
            else:
                exisitingchars += 1
            temp = temp.children[index]
        return exisitingchars

