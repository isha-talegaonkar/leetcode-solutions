# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        level = 0
        queue = deque([root])
        
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
        
        for i in range(len(levels)):
            if i % 2 == 0:
                continue
            else:
                levels[i] = levels[i][::-1]
        return levels