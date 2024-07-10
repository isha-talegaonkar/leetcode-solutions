# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, left, right):
            if node is None:
                return True

            if node.val <= left or node.val>=right:
                return False

            return isValid(node.right, node.val, right) and isValid(node.left, left, node.val)
    
        
        return isValid(root, float("-inf"), float("+inf"))

        