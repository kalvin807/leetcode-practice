# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        comp = set()
        queue = [root]
        while len(queue):
            node = queue.pop()
            need = k - node.val
            if need in comp:
                return True
            comp.add(node.val)
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
        return False
        # speed O(n), space O(n)
