
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
k = 3
nums = [4,5,8,2]
vals = [3,5,1,9,4]

obj = KthLargest(k, nums)
for val in vals:
    print(f'Min heap is now: {obj.add(val)}')

