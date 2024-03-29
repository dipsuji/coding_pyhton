from typing import List


class Solution:
    """
    You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where
     each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the
     sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.

    Example 1:

    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)
    Example 2:

    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)
    Example 3:

    Input: people = [3,5,3,4], limit = 5
    Output: 4
    Explanation: 4 boats (3), (3), (4), (5)

    """

    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1

        boats_number = 0

        while left <= right:
            if left == right:
                boats_number += 1
                break
            if people[left] + people[right] <= limit:
                print("inside----------------")
                left += 1
            print("OTSIDE----")
            print("AND----")
            right -= 1
            boats_number += 1
        return boats_number


s = Solution()
answer = s.num_rescue_boats([1, 1, 2, 3, 1], 3)
# 1, 1, 1, 2, 3
# 0, 1, 2, 3, 4
print(answer)
