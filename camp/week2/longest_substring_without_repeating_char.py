# questionurl : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast = slow = maxlen = 0

        uniques = set()

        while fast < len(s) and slow <= fast:
            if s[fast] in uniques:
                uniques.remove(s[slow])
                slow += 1
            else:
                uniques.add(s[fast])
                fast += 1

                if fast - slow > maxlen: maxlen = fast - slow
        return maxlen
