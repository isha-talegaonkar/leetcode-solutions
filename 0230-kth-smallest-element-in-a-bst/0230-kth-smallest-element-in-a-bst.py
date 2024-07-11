# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traversal(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return []
            
            return traversal(node.left) + [node.val] + traversal(node.right)
        
        return traversal(root)[k-1]