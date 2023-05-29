class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        new_word = []
        limit = len(s) - 1

        for letter in s:
            if letter not in vowels:
                new_word.append(letter)
            else:
                for idx in range(limit, -1, -1):
                    letter_vowel = s[idx]
                    if letter_vowel in vowels:
                        new_word.append(letter_vowel)
                        limit = idx - 1
                        break

        return ''.join(new_word)


"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""