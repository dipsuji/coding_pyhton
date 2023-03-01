"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from collections import defaultdict
from typing import List


class Solution:
    def contains_duplicate1(self, nums: List[int]) -> bool:
        """
        n(log(n))
        Using sort with one loop
        :param nums:
        :return:
        """
        nums.sort()  # n(log(n))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def contains_duplicate2(self, nums: List[int]) -> bool:
        """
        O(n), space = O(n)
        Using sort with one loop
        :param nums:
        :return:
        """
        o = set(nums)  # n(log(n))
        if len(nums) != len(s):
            return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        O(n), space = O(n)
        Optomize solutions with hash map
        :param nums:
        :return:
        """
        m = defaultdict(int)

        for num in nums:
            if m[num]:
                return True
            m[num] += 1
        return False


num1 = [2, 11, 11, 7, 15]
# num1 = [2, 11, 7, 15]
s = Solution()
answer = s.contains_duplicate1(num1)
print(answer)
answer1 = s.contains_duplicate1(num1)
print("With using set--------------")
print(answer1)
answer2 = s.containsDuplicate(num1)
print("WITH Optimize solutions----------------")
print(answer2)
