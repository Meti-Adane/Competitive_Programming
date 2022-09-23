class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = (10**9) + 7
        arr = []
        
        for i in range(1, n+1):
            arr.append(bin(i)[2:])
        ans = "".join(arr)
        return int(ans, 2) % mod