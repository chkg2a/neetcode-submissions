class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap) > 1:
            first_num = -heap[0]
            second_num = -heap[1]
            if first_num == second_num:
                heapq.heappop(heap)
                heapq.heappop(heap)
            if first_num > second_num:
                third_num = -(first_num - second_num)
                heapq.heappop(heap)
                heapq.heappop(heap)
                heapq.heappush(heap,third_num)

        return -heap[0] if len(heap) >= 1 else 0
