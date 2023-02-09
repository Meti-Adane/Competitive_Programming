class Solution:
    def maximumSwap(self, num: int) -> int:
        swapIdx = place = 1
        significantDigit = float('-inf')
        ans = copy = num

        while num > 0:
            digit = num % 10
            num //= 10

            if significantDigit > digit:
                newNumber = (copy - (digit*place) - (swapIdx*significantDigit) + 
                            (digit*swapIdx) + (significantDigit*place))
                ans = max (ans, newNumber)

            if digit > significantDigit:
                significantDigit, swapIdx = digit, place

            place *= 10
        return ans 
            