"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
from typing import List


class Solution:

    def backtracking(self, ans, keyboard_number_latter_map, digits_str, combination, index):
        # if index > len(digits_str):
        #     print("return BASE CASE digit_str  " + digits_str)
        #     print("index :  " + str(index))
        #     return
        if len(combination) == len(digits_str):
            print(f"return got combination  len(combination) == len(digits_str)---{combination}   index - {index}")
            ans.append(combination[:])
            return

        currentDigit = digits_str[index]
        curString = keyboard_number_latter_map[currentDigit]
        print(f"current digit:---> {currentDigit}     and     curSting:--- {curString}")
        for i in range(len(curString)):
            print(f"breaking branches: ---------- {i}")
            self.backtracking(ans, keyboard_number_latter_map, digits_str, combination +
                              curString[i], index + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return ans

        m = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        self.backtracking(ans, m, digits, "", 0)

        return ans


nums = "23"
# nums = ""
s = Solution()
answer = s.letterCombinations(nums)
print(answer)
