# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        self.pre_idx = 0
        self.inorder_map = {
            value: index
            for index, value in enumerate(inorder)
        }

        def DFS(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = self.inorder_map[root_val]

            root.left = DFS(left, mid - 1)
            root.right = DFS(mid + 1, right)

            return root

        return DFS(0, len(inorder) - 1)
