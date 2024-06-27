# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkIfBalanced(self, root: Optional[TreeNode]) -> (bool, int):
        if root is None:
            return True, -1
        
        leftIsBalanced, leftHeight = self.checkIfBalanced(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.checkIfBalanced(root.right)
        if not rightIsBalanced:
            return False, 0
        
        return (abs(leftHeight-rightHeight) < 2), 1+max(leftHeight, rightHeight)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkIfBalanced(root)[0]

            
        