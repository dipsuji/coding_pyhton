"""
- https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0)+1
        for num in nums:
            if(m[num]>len(nums)//2):
                return num


num1 = [2, 11, 11, 7, 11] # list length = 5, half = 2.5, ans - element have more than 2 times.
# num1 = [2, 11, 7, 15]
s = Solution()
answer = s.majorityElement(num1)
print(answer)
