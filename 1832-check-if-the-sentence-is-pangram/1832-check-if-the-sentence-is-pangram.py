class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = { chr(i) for i in range(97, 123)}
        for char in sentence:
            letters.discard(char)
        return len(letters) == 0