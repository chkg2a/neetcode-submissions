class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        c = Counter(students)
        for s in sandwiches:
            if c[s] > 0:
                res -= 1
                c[s] -=1
            else:
                return res
        return res