from typing import Optional, List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = []
        p = 0
 
        if  m == 0:
            nums1.pop()
            nums1.append(nums2[0])
        elif not n:
            return nums1
        print('ok')
        # m = m-1
        i = 0
        k = 0
        while True:

            if nums1[i] >= nums2[k]:
                print('if',nums1[i],nums2[k])
                nums1.insert(i+1, nums2[k])
                nums1.pop()
                k = k + 1
                i = i + 1
                print(nums1)
            else:
                # nums1.insert(i+1, nums2[k])
                # nums1.pop()
                # k = k + 1
                print('else',nums1[i],nums2[k])
                # pass
                i = i + 1

            if i == m or k == n:
                break
        return nums1





nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1,m,nums2, n))
# Output: [1,2,2,3,5,6]
