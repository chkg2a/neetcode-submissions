class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ""
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            m_freq, m_char = heapq.heappop(max_heap)
            m_freq += 1
            res += m_char
            if prev:
                heapq.heappush(max_heap,prev)
                prev = None
            if m_freq != 0:
                prev = [m_freq,m_char]
        return res