class Solution:
    def frequencySort(self, s: str) -> str:
        
        return "".join([ch*fq for fq, ch in sorted([(fq, ch) for ch, fq in Counter(s).items()], reverse=True)])