from typing import List


class Solution:
    """
    Given an array of integers arr, return true if and only if it is a valid mountain array.
    Example 1:

    Input: arr = [2,1]
    Output: false
    Example 2:

    Input: arr = [3,5,5]
    Output: false
    Example 3:

    Input: arr = [0,3,2,1]
    Output: true
    """
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        i = 1
        while i < len(A) and A[i] > A[i - 1]:
            i += 1

        if i == 1 or i == len(A):
            return False

        while i < len(A) and A[i] < A[i - 1]:
            i += 1

        return i == len(A)


s = Solution()
answer = s.validMountainArray([1, 1, 2, 3, 1])
print(answer)
