# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        path = []
        def preOrder(node):
            if node:
                path.append(str(node.val))
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        return ",".join(path)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
            pre-order format,
            seperated by comma
        """
        if not data:
            return None
        queue = deque([int(n) for n in data.split(",")])
        def buildTree(lower, upper):
            if queue and lower < queue[0] < upper:
                v = queue.popleft()
                node = TreeNode(v)
                node.left = buildTree(lower, v)
                node.right = buildTree(v, upper)
                return node
        return buildTree(-float("inf"), float("inf"))
                      
            

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
