# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        if not root:
            return levels
        
        queue = deque([root])
        
        level = 0
        
        while queue:
            levels.append([])
            levelLength = len(queue)
            for i in range(levelLength):
                node = queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
        
        return levels
        
#         levelsList = []
        
#         if not root:
#             return list(levelsList)
        
#         def helper(node: TreeNode, level):
#             if len(levelsList) == level:
#                 levelsList.append([])
                
#             levelsList[level].append(node.val)
            
#             if node.left:
#                 helper(node.left, level+1)

#             if node.right:
#                 helper(node.right, level+1)
        
#         helper(root, 0)
#         return levelsList