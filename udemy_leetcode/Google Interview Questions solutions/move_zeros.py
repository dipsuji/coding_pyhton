# from typing import List
#
#
# class Solution:
#     """
#     Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#     Example 1:
#
#     Input: nums = [0,1,0,3,12]
#     Output: [1,3,12,0,0]
#
#     Example 2:
#
#     Input: nums = [0]
#     Output: [0]
#
#     """
#
#     def moveZeroes(self, nums: List[int]) -> list[int]:
#         j = 0
#         for num in nums:
#             if (num != 0):
#                 nums[j] = num
#                 j += 1
#
#         for x in range(j, len(nums)):
#             nums[x] = 0
#
#         return nums
#
#
# input_arr = [0, 1, 0, 3, 12]
# s = Solution()
# result = s.moveZeroes(input_arr)
# print(result)


List= []
n = int(input("Enter the no. of elements in the array! "))
for i in range(0,n):
    a= int(input())
    List.append(a)
j=0

for i in range(n):
    if List[i]!=0:
        List[j]=List[i]
        j+=1


while j<n:
    List[j] = 0
    j+=1

print(List)