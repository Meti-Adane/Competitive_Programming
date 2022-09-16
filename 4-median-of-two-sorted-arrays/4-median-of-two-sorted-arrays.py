class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2) 
        m = n // 2 
        nums1.append(10**6+1)  # to keep em in bound yuppp i got lazy endgi 
        nums2.append(10**6+1)
        targetIdx = m if (n % 2 != 0) else m-1
        left, right = 0, 0
        ans = 0 
        i = 0 
        while i <= targetIdx:
            if nums1[left] <= nums2[right]:
                ans = nums1[left]
                left += 1
            else:
                ans = nums2[right]
                right += 1
            i += 1
        if n % 2 != 0 :
            return ans 
        
        return (ans + min(nums1[left], nums2[right])) / 2
        