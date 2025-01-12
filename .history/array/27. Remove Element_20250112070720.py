from types import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        c=0
        r = len(nums)-1
        l = 0
        while True:
            print(nums)
            if l>=r:
                break
            if nums[r] == val:
                r=-1
            if nums[l] != val:
                l+=1
            
            if nums[r] != val and nums[l] == val:
                nums[l] = nums[r] 
                nums[r] = val
                c+=1
        return c

s = Solution()
nums = []
val = 2
print(s.removeElement(nums, val))