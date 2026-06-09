# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lcaa = [root]

        def lca(root):
            if root is p or root is q:
                return 
        
            lcaa[0] = root
            if root.val < q.val and root.val < p.val:
                return lca(root.right)
            elif root.val > q.val and root.val > p.val:
                return lca(root.left)
            else:
                return

        lca(root)
        return lcaa[0]

        
        
        
