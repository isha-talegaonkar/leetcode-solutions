# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        val = ""
        if root == None:
            return "X,"

        leftSerialize = self.serialize(root.left)
        rightSerialize = self.serialize(root.right)

        return str(root.val) + "," + leftSerialize + rightSerialize
        

    def deserialize(self, data):
    
        def deserializeHelper(queue):
            element = queue.popleft()
            if element == "X":
                return None
        
            node = TreeNode(int(element))
            node.left = deserializeHelper(queue)
            node.right = deserializeHelper(queue)
            
            return node
            
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        queue = deque(data.split(","))

        return deserializeHelper(queue)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))