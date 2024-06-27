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
        
        queue = deque([root])
        result = []
        
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                
                if i == length -1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return result
                    