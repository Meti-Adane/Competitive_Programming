# question url: https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPointer = 0
        suffixPointer = len(nums) - 1
        output = []

        prefixarr = []
        suffixarr = []

        for i in range(len(nums) - 1):
            if prefixPointer == 0 and suffixPointer == len(nums) - 1:
                prefixarr.append(nums[prefixPointer])
                suffixarr.append(nums[suffixPointer])
            else:
                prefixprod = nums[prefixPointer] * prefixarr[i - 1]
                sufixprod = nums[suffixPointer] * suffixarr[i - 1]

                prefixarr.append(prefixprod)
                suffixarr.append(sufixprod)
            prefixPointer += 1
            suffixPointer -= 1

        arrSize = len(suffixarr)
        for j in range(len(nums)):
            if j == 0:  # no prefix
                output.append(suffixarr[arrSize - j - 1])
            elif j == len(nums) - 1:
                output.append(prefixarr[-1])
            else:
                val = (prefixarr[j - 1]) * (suffixarr[arrSize - j - 1])
                output.append(val)

        return output
