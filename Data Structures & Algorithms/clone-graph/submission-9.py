"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        o_t_n = {}
        start = node
        stk = [start]
        visit = set()
        visit.add(start)


        while stk:
            node = stk.pop()
            o_t_n[node] = Node(val = node.val)
            
            for nei in node.neighbors:
                if nei not in visit:
                    stk.append(nei)
                    visit.add(nei)

        for old_node, new_node in o_t_n.items():
            for nei in old_node.neighbors:
                new_nei = nei
                new_node.neighbors.append(o_t_n[new_nei])

        return o_t_n[start]