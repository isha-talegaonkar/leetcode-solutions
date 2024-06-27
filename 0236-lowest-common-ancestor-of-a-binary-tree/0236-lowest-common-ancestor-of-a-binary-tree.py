# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(currentNode: 'TreNode') -> bool:
            if not currentNode: 
                return False
            
            left = traverse(currentNode.left)
            right = traverse(currentNode.right)
            
            mid = currentNode == p or currentNode == q
            
            if mid + left + right >= 2:
                self.ans = currentNode
            
            return mid or left or right
        
        traverse(root)
        return self.ans
                