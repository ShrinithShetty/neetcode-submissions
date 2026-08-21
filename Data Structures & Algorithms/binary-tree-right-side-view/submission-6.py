# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        ans = []

        while q:
            n = len(q)
            rightside = None
            for i in range(n):
                node = q.popleft()
                if node:
                    rightside = node.val
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)

            if rightside:
                ans.append(rightside)
        return ans
        
            