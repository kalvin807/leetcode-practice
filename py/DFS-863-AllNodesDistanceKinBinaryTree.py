# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def dfs(self, node, parent, parentDict):
        parentDict[node] = parent
        if node.left:
            self.dfs(node.left, node, parentDict)
        if node.right:
            self.dfs(node.right, node, parentDict)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Dict to map the parent of a Node
        parentDict = {}
        self.dfs(root, None, parentDict)  # O(N), N = all node in tree

        distance = 0
        seen = set()
        queue = collections.deque([target])
        while len(
            queue
        ):  # BFS, O(N), N = all node in tree, worse case distance equal farest Node
            if distance == k:  # when distance == k
                # all node in queue equal to distance k
                # return them as answer
                return [n.val for n in queue]
            # Explore all node in this layer
            for _ in range(len(queue)):
                node = queue.popleft()
                # Add all nearby node, left ,right and parent
                if node.left and node.left not in seen:
                    queue.append(node.left)
                if node.right and node.right not in seen:
                    queue.append(node.right)
                if pNode := parentDict.get(node, None):
                    if pNode not in seen:
                        queue.append(pNode)
                seen.add(node)
            distance += 1

        # Exhausted all node but didnt reach wanted dist, return empty
        return []
