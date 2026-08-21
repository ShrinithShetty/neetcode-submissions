# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        val = [root.val]
        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)

            val[0] = max(val[0], root.val + leftmax + rightmax)

            return root.val + max(leftmax, rightmax)
        dfs(root)
        return val[0]

        
        