# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        checked = []

        while True:
            checked.append(head.val)

            if not head.next:
                break

            head = head.next

        return True if checked == checked[:: -1] else False


"""
234. Palindrome Linked List
Easy
15.2K
815
Companies
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
Accepted
1.6M
Submissions
3.1M
Acceptance Rate
50.9%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (114)
Similar Questions
Palindrome Number
Easy
Valid Palindrome
Easy
Reverse Linked List
Easy
Maximum Twin Sum of a Linked List
Medium
Related Topics
Linked List
Two Pointers
Stack
Recursion
"""