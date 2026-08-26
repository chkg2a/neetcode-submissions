class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        current = []
        for i in nums1:
            if i not in nums2:
                current.append(i)
        res.append(current)
        current = []
        for i in nums2:
            if i not in nums1:
                current.append(i)
        res.append(current)
        return res