def intersection(self, nums1, nums2) -> int:
    intersection = []
    for i in nums1:
        if i in nums2 and i not in intersection: intersection.append(i)
    return intersection