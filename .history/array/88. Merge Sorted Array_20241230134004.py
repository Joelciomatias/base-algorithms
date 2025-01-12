from typing import Optional, List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i = 0
        # k = 0
        # while True:
        #     if (i+k) == m+1:
        #         nums1 = nums1[:i+1] + nums2[k:]
        #         break
        #     elif nums1[i] >= nums2[k]:
        #         nums1.insert(i+1, nums2[k])
        #         nums1.pop()
        #         k = k + 1
        #         i = i + 1
        #     else:
        #         i = i + 1
        #     if i == n:
        #         break
        k = m+n -1
        # k = m
        # n = n 
        m = m - 1
        n = n - 1
        for i in range(m+n):
         
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1

        return nums1





nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
print(Solution().merge(nums1,m,nums2, n))
# Output: [1,2,2,3,5,6]
