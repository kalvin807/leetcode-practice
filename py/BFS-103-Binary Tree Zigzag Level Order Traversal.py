# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        LtoR = True  # Flip direction
        queue = collections.deque([root])
        levels = []
        while len(queue):
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            if not LtoR:
                layer.reverse()  # Flip the ans if it is R to L
            levels.append(layer)
            LtoR = not LtoR  # Flip
        return levels
