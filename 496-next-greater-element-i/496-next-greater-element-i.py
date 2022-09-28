class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums1))]
        hashmap = { val:i for i, val in enumerate(nums1)}
        stack = []
        
        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                if stack[-1] in hashmap:
                    ans[hashmap[stack[-1]]] = num
                stack.pop()
            stack.append(num)
        return ans