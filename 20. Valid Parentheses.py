class Solution:
    def isValid(self, s: str) -> bool:
        check_open = {'(', '{', '['}
        check_pairs = {')': '(', '}': '{', ']': '['}
        stack_parent = [s[0], ]

        if len(s) % 2 == 1:
            return False

        for parent in s[1:]:
            if parent in check_open:
                stack_parent.append(parent)
                continue
            if stack_parent:
                if stack_parent[-1] == check_pairs[parent]:
                    stack_parent.pop()
                else:
                    return False
            else:
                return False

        return True if len(stack_parent) == 0 else False


"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""