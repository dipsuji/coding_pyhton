from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(0, n):
            goal = target - nums[i]
            if (goal in m):
                return [m[goal], i]
            m[nums[i]] = i

    def twoSumBruitForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            goal = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] == goal:
                    return [i, j]


num1 = [2, 11, 7, 15]

# 24, 13, 17, 11

num2 = 26    # 11, 15
s = Solution()
answer = s.twoSum(num1, num2)
print(answer)
answer1 = s.twoSumBruitForce(num1, num2)
print("WITH TWO LOOP")
print(answer1)


