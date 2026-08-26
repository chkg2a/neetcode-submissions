class Solution:
    def isPathCrossing(self, path: str) -> bool:
        walked = [[0,0]]
        for ch in path:
            current_path = walked[-1].copy()
            if ch == "N":
                current_path[1] += 1
            if ch == "S":
                current_path[1] -= 1
            if ch == "E":
                current_path[0] += 1
            if ch == "W":
                current_path[0] -= 1
            if current_path in walked:
                return True
            walked.append(current_path)
        return False
            