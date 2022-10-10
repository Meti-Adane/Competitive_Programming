class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        word = list(palindrome)
        if n == 1:
            return ""
        for i in range(n//2):
            if word[i] != "a":
                word[i] = "a"
                return "".join(word)
        word[-1] = 'b'
        return "".join(word)