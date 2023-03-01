"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

"""

class Solution(object):
    def single_number(self, nums):
        """
        Suppose input = [a, b, c, a, b]
        -> if all duplicate then equation will be - 2(a+b+c)
        -> input is 2a+2b+c

        O(n)
        Space - O(n)
        :type nums: List[int]
        :rtype: int
        """
        set_num = set(nums) # only unique element

        return 2*sum(set_num)-sum(nums)

    def single_number_xor(self, nums):
        """
        Suppose input = [a, b, c, a, b]
        -> if all duplicate then equation will be - 2(a+b+c)
        -> input is 2a+2b+c

        O(n)
        Space - O(n)
        :type nums: List[int]
        :rtype: int
        """
        final = 0

        for num in nums:
            # print("final--------------------")
            # print(final)
            final ^= num

        return final


input_arr = [4, 4, 2, 2, 1]
s = Solution()
answer = s.single_number(input_arr)
answer_xor = s.single_number_xor(input_arr)
print(answer)
print("answer_xor----")
print(answer_xor)