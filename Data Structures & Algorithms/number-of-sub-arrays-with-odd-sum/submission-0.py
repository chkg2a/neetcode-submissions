class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        subArr = []
        mod = 1000000007
        for i in range(len(arr)):
            current = []
            for j in range(i, len(arr)):
                current = current + [arr[j]]
                subArr.append(current)
        print(subArr)
        count = 0
        for arr in subArr:
            if sum(arr) % 2 == 1:
                count += 1 % mod
        return count