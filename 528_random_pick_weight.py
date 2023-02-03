import bisect
import random 
class Solution:

    def __init__(self, w: List[int]):
        self.prefixsum = list(accumulate(w))
        self.totalSum = self.prefixsum[-1]

    def pickIndex(self) -> int:
        randomNum = random.randint(1, self.totalSum)
        idx = bisect.bisect_left(self.prefixsum, randomNum)
        return idx 
