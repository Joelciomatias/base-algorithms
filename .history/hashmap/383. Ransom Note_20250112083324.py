class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        pass



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

# nums = [2]
# val = 3
# [2]

print(s.canConstruct(nums, val))