"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

"""
from typing import List


class Solution:
    def four_sum_count(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = {}
        ans = 0

        for i in range(0, len(A)):
            x = A[i]
            for j in range(0, len(B)):
                y = B[j]
                if x + y not in m:
                    m[x + y] = 0
                m[x + y] += 1

        for i in range(0, len(C)):
            x = C[i]
            for j in range(0, len(D)):
                y = D[j]
                target = -(x + y)
                if target in m:
                    ans += m[target]

        return ans


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
s = Solution()
answer = s.four_sum_count(nums1, nums2, nums3, nums4)
print(answer)
