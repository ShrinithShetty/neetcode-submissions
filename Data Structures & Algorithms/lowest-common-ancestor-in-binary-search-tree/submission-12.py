# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def search(root):
            if root is p or root is q:
                return

            lca[0] = root

            if root.val > q.val and root.val > p.val:
                return search(root.left)
            elif root.val < q.val and root.val < p.val:
                return search(root.right)


            else:
                return

        search(root)
        return lca[0]
        