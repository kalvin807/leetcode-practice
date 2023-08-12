# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

# BFS
# The serialized stuff is in format of "1,2,#,#" where "#" mean null and "," is seperator
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        serialized = ""
        queue = collections.deque([root])
        while len(queue):
            node = queue.popleft()
            if node:
                serialized += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized += "#"
            serialized += ","
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def make_node(val):
            return None if val == "#" else TreeNode(val)

        # Null is represented by "#"
        if not len(data) or data == "#":
            return None
        data = data.split(",")
        head = make_node(data[0])
        queue = collections.deque([head])
        i = 1
        # This loop assume the data is always complete and valid
        # So that i will be the end of data when the queue is empty
        while len(queue):
            parent = queue.popleft()
            # Take two val and attach to parent
            parent.left = make_node(data[i])
            parent.right = make_node(data[i + 1])
            i += 2
            # add to queue if then not None
            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)
        return head


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
