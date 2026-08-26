class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strr = int("".join(str(d) for d in digits)) + 1
        return [int(x) for x in str(strr)]