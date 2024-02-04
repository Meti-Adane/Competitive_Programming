class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        N, count = len(s), len(lookup)
        start = 0
        ans, minLength = s, N+1

        for i, char in enumerate(s):
            if char in lookup:
                lookup[char] -= 1
                if lookup[char] == 0: count -= 1

            while start < i and (s[start] not in lookup or lookup[s[start]] < 0):
                if s[start] in lookup: lookup[s[start]] += 1
                start += 1

            if count == 0 and (i-start+1) < minLength:
                ans, minLength = s[start:i+1], (i-start+1)

        return ans if count == 0 else ""