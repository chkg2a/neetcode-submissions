class CountSquares:

    def __init__(self):
        self.hm = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.hm[tuple(point)] += 1
        self.pts.append(point)
        
    def count(self, point: List[int]) -> int:
        cnt = 0
        qx, qy = point
        for x, y in self.pts:
            if (abs(qy- y) != abs(qx - x)) or x == qx or y == qy: 
                continue
            cnt += self.hm[(x,qy)] * self.hm[(qx,y)]
        return cnt