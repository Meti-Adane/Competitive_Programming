class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for i in range(1, 9):
            num = ""
            for j in range(i, 10):
                num += str(j)
                convertedNum = int(num)
                if convertedNum > high:
                    break
                if low <= convertedNum and convertedNum <= high:
                    ans.append(convertedNum)
        return sorted(ans) 