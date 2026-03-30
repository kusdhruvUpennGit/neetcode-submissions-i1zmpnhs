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
        
        oldToNew = {}

        def dfs(curr):
            
            if curr in oldToNew:
                return oldToNew[curr]
            
            copy = Node(curr.val)
            oldToNew[curr] = copy
            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)