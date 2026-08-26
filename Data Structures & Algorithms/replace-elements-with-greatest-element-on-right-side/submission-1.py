class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr)):
            next_greatest = max(arr[i:])
            if arr[i] == next_greatest and i < len(arr) - 1:
                next_greatest = max(arr[i + 1:])
            stack.append(next_greatest)
        stack[-1] = -1
        return stack