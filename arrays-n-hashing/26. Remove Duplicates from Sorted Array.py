
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return len(nums)
        # l = 0
        # r = 1
        # le = len(nums)-1
        # while l < le:
        #     if nums[l] == nums[r]:
        #         ele = nums.remove(l)
        #         # k = r
        #         # while k < le:
        #         #     a = nums[k]
        #         #     nums[k] = nums[k+1]
        #         #     nums[k+1] = a
        #         #     k +=1
        #         le-=1
        #     else:
        #         r+=1
        #         l+=1
        # return r
        l=1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
            


        
nums = [1,1,2]
# Output: 2, nums = [1,2,_]


nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]]

s = Solution()
print(s.removeDuplicates(nums))