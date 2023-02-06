class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hashMap = defaultdict(int)
        ans = 1
        words = sorted(words, key = lambda x:len(x)) 
        for i, word in enumerate(words):
            if not hashMap[word]:
                hashMap[word] = 1
            for j, char in enumerate(word):
                predecessor = word[:j]+''+word[j+1:]
                hashMap[word] = max(hashMap[predecessor]+1, hashMap[word])
                ans = max(ans, hashMap[word])
        return ans