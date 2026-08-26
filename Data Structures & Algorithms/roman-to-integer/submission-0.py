class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        final_value = 0
        for i in range(len(s) - 1):
            if "C" == s[i] and (s[i+1] == "D" or s[i+1] == "M"):
                final_value -= hashMap[s[i]]
            elif "X" == s[i] and (s[i+1] == "L" or s[i+1] == "C"):
                final_value -= hashMap[s[i]]
            elif "I" == s[i] and (s[i+1] == "V" or s[i+1] == "X"):
                final_value -= hashMap[s[i]]
            else:
                final_value += hashMap[s[i]]

        final_value += hashMap[s[len(s) - 1]]
            
        return final_value