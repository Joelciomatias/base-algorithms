from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        c=0
        r = len(nums)-1
        l = 0
        while True:
            if l>=r:
                break
            if nums[r] == val:
                r-=1
            if nums[l] != val:
                l+=1
            
            if nums[r] != val and nums[l] == val:
                nums[l] = nums[r] 
                nums[r] = val
                c+=1
        print(c)

        return len(nums)-c


s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
#Output: 2, nums = [2,2,_,_]

nums = [3,2,2,3]
val= 3
#  2, nums = [2,2,_,_]

nums = [1]
val = 1
# 0, []

nums = [2]
val = 3
# [2]

print(s.removeElement(nums, val))