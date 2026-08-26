class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = [0] * k
        remainder_count[0] = 1

        remainder_sum = 0
        total_subarr = 0
        for num in nums:
            remainder_sum += num
            remainder = remainder_sum % k
            total_subarr += remainder_count[remainder] 
            remainder_count[remainder] += 1
        return total_subarr

