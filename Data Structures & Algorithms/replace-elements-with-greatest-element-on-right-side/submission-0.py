class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr)):
            next_greatest = max(arr[i:]) 
            stack.append(next_greatest)
        stack[-1] = -1
        return stack