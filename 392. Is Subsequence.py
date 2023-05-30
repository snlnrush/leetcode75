class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        sub_str_list = list(s)[:: - 1]
        for letter in t:
            if sub_str_list[-1] == letter:
                sub_str_list.pop()
            if not sub_str_list:
                return True
        return False


"""

392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""