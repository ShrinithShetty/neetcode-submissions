# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = [0]
        

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)

            diameter = left + right

            length[0] = max(length[0], diameter)

            return max(left, right) + 1

        depth(root)
        return length[0]