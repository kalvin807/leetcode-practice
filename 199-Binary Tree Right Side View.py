# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        path = []
        queue = collections.deque([root])
        while queue:
            righmost = None
            for _ in range(len(queue)):
                node = queue.popleft()
                rightmost = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            path.append(rightmost)
        return path
