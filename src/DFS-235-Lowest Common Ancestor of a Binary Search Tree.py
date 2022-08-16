# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(node, target, path):
            if node:
                path.append(node)
                if node == target:
                    return path
                if node.val > target.val:
                    return find_path(node.left, target, path)
                else:
                    return find_path(node.right, target, path)
        
        path_p = find_path(root, p, [])
        path_q = find_path(root, q, [])
        last = root
        for node_p, node_q in zip(path_p, path_q):
            if node_p.val != node_q.val:
                return last
            else:
                last = node_p
        return last
