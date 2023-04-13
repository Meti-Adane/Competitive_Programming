class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        ans = [-1 ] * len(nums1)
        stack = []
        for pos, num in enumerate(nums1):
            hashmap[num] = pos
        for num in nums2:
            while stack and num > stack[-1]:
                target = stack.pop()
                if target in hashmap:
                    ans[hashmap[target]] = num
            stack.append(num)
        return ans