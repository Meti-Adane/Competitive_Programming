class Solution:
    def numberToWords(self, num: int) -> str:
        lookup = {
            1000000000: "Billion",
            1000000: "Million",
            1000: "Thousand",
            100: "Hundred",
            90: "Ninety",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6: "Six",
            5: "Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
            0: "Zero",
        }
        if num == 0: return lookup[0]
        
        nums = [float("inf"), 1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20]
        
        def recurse(num, lookup, nums):
            ans = deque()
            for i in range(1,len(nums)):
                if nums[i] <= num < nums[i-1]:
                    quotient, remainder = num // nums[i], num % nums[i]
                    ans.append(lookup[nums[i]])

                    if remainder > 0: ans.append(recurse(remainder, lookup, nums))
                   
                    if quotient > 0 and i < 5: ans.appendleft(recurse(quotient, lookup, nums))
                    return " ".join(ans)
            return lookup[num]
            
        return recurse(num, lookup, nums)