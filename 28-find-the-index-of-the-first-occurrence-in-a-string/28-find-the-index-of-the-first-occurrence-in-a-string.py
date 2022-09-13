class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        d = len(needle)
        while left+d <= len(haystack):
            if haystack[left:left+d] == needle:
                return left
            left += 1
        return -1