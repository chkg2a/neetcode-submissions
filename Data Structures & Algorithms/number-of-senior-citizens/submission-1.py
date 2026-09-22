class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for strr in details:
            age = int(strr[-4:-2])
            print(age)
            if age > 60:
                count += 1
        return count