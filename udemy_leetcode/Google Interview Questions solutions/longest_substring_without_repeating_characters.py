class Solution:
    """
    Given a string s, find the length of the longest substring
    without repeating characters.
    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def length_Of_longest_substring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while left < n and right < n:
            el = s[right]
            if el in m:
                left = max(left, m[el] + 1)
            m[el] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans


s = Solution()
answer = s.length_Of_longest_substring("abcabcbb")
print(answer)
