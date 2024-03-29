"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""

class Solution(object):
    def addBinary(self, a, b):
        result = []
        carry = 0
        i = len(a)-1
        j = len(b)-1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total//2

        return ''.join(reversed(result))


str1 = "1010"
str2 = "1011"
s = Solution()
answer = s.addBinary(str1, str2)
print(answer)