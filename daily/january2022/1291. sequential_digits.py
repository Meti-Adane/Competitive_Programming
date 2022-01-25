class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        ans = []
        k = len(str(low))
        while k <= len(str(high)):
            left, right = 0, 0+k
            while right <= len(digits):
                num = int(digits[left:right])
                if int(num) > high:
                    break
                if int(num) >= low:
                    ans.append(num)
                left += 1
                right += 1
            k += 1
        return ans            