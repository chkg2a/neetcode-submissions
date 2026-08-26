class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums) 
        print(count)
        for key, value in count.items():
            if value < 2:
                return False
        
        return True