
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        counter = Counter(words) 
        heap = [] 
        ans = []
        
        for word, freq in counter.items(): 
            heappush(heap, (-1 * freq, word))
        
        while k: 
            ans.append(heappop(heap)[1])
            k -= 1
        return ans 
    
    