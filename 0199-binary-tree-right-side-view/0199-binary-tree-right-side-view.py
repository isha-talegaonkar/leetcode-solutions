# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root])
        rightSide = []
        
        while next_level:
            curr_level = next_level
            next_level = deque()
            
            while curr_level:
                node = curr_level.popleft()
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            rightSide.append(node.val)
        
        return rightSide
        