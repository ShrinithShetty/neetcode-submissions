# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = [0]


        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            diameter = left + right

            longest[0] = max(longest[0],diameter)

            return 1 + max(left,right)

        height(root)
        return longest[0]