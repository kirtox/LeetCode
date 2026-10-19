from collections import deque
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

        dq = deque([root])
        res = []

        while dq:
            level_size = len(dq)
            level_nums = []

            for _ in range(level_size):
                curr = dq.popleft()
                level_nums.append(curr.val)

                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

            res.append(level_nums)
        return res

# O(n) time complexity, O(n) space complexity