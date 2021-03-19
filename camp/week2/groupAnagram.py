# question url : https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        asciiDict = dict()
        anagram_group = []
        for word in strs:
            if asciiDict.get(tuple(sorted(word))):
                asciiDict[tuple(sorted(word))].extend([word])
            else:
                asciiDict[tuple(sorted(word))] = [word]
        return dict.values(asciiDict)