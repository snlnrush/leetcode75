class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pre, m_string = (str1, str2) if len(str1) <= len(str2) else (str2, str1)
        base = len(pre)
        main = len(m_string)
        div, path = divmod(main, base)

        while True:
            if base == 0:
                return ''
            if div == 0:
                return ''
            if path == 0:
                if m_string == pre * div:
                    return pre
                base -= 1
                pre = pre[: base]
            else:
                base -= 1


"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""