# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, target, path):
        if node == None:
            return None
        path.append(node)
        if node == target:
            return path
        if res := self.dfs(node.left, target, path):
            return res  
        if res := self.dfs(node.right, target, path):
            return res
        path.pop()
        return None 
            
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.dfs(root, p, [])
        path_q = self.dfs(root, q, [])
        # LCA == Last common node in path root -> p and path root -> q
        lca = None
        for step_p, step_q in zip(path_p, path_q):
            if step_p.val == step_q.val:
                lca = step_p
            else:
                break
        return lca
    # Time complexity O(L) where L is the level of the longer path of p or q
    # Space complexity O(P + Q) where P and Q is the number of nodes in path of p and q
