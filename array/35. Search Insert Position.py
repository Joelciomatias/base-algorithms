from curses.ascii import SO
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        r = 1
        for i in range(len(nums)):
            print(f'r: {r}, i: {i}')
           
            if nums[i] > target or nums[i] == target:
                return i

            if r >= len(nums):
                return r
            r += 1
print(Solution().searchInsert([1,3,5,6],7))