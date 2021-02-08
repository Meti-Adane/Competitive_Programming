# question url: https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[(self.k ) * -1]