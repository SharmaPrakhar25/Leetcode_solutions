# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        output = []
        output.append(root.val)
        leftValue = self.preorderTraversal(root.left)
        rightValue = self.preorderTraversal(root.right)
        return output + leftValue + rightValue
    
#     def preOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         staK = []
#         stak.append(root)
#         while len(stak) > 0:
#             currentRoot = stak[-1]
#             print(currentRoot.val)
#             if currentRoot.left is not None:
#                 stak.append(currentRoot.left)
            
#         return