
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return sorted(counter, key=lambda x:(-counter[x], x))[:k]
    
    