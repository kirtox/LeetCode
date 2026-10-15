# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        level_dict = {}

        stack = [(root, 1)]

        while stack:
            # tmp = stack.pop()
            # curr, depth = tmp[0], tmp[1]
            curr, depth = stack.pop()
            
            if level_dict.get(depth, -1) != -1:
                level_dict[depth].append(curr.val)
            else:
                level_dict[depth] = [curr.val]

            
            if curr.right:
                stack.append((curr.right, depth + 1))
            if curr.left:
                stack.append((curr.left, depth + 1))

        return list(level_dict.values())

# O(n) time complexity, O(n) space complexity