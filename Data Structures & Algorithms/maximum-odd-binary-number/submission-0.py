class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        res = ""
        while cnt["1"] > 1:
            res+="1" 
            cnt["1"] -=1
        while cnt["0"] > 0:
            res += "0"
            cnt["0"]  -= 1
        if cnt["1"] == 1:
            res += "1"
        return res 