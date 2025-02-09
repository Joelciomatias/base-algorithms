import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                n = (y - x)
                heap.append(n)
                heapq.heapify(heap)

        return 0 if not heap else -heap[0]

v = [2,7,4,1,8,1]
s = Solution()
print(f'result: {s.lastStoneWeight(v)}')