# question url : https://leetcode.com/contest/weekly-contest-80/problems/most-common-word/

import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = re.sub("[!?',;.]", ' ', paragraph.lower())
        words = words.split(" ")
        counterDict = dict()

        for word in words:
            if word not in banned and word.isalpha():
                counterDict[words.count(word)] = word

        return counterDict[max(dict.keys(counterDict))]