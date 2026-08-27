class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        size = m + n - 1
        m = m - 1
        n = n - 1
        while size >= 0 and m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[size] = nums1[m]
                m -= 1
            elif nums2[n] >= nums1[m]:
                nums1[size] = nums2[n]
                n -= 1
            size -= 1
        while n >= 0 and size >= 0:
            nums1[size] = nums2[n]
            n -=1
            size -=1
