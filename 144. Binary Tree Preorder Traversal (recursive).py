# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        It's recursive solution
        """
        traversed_values = []

        def pre_order_trav(self, current_node):
            if current_node:
                traversed_values.append(current_node.val)
                pre_order_trav(self, current_node.left)
                pre_order_trav(self, current_node.right)

        pre_order_trav(self, root)

        return traversed_values


"""
144. Binary Tree Preorder Traversal
Easy
7.5K
193
Companies
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

Accepted
1.4M
Submissions
2.1M
Acceptance Rate
68.2%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (55)
Similar Questions
Binary Tree Inorder Traversal
Easy
Verify Preorder Sequence in Binary Search Tree
Medium
N-ary Tree Preorder Traversal
Easy
Kth Largest Sum in a Binary Tree
Medium
Related Topics
Stack
Tree
Depth-First Search
Binary Tree
"""