class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(start: int):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res

# O(n! * n) time complexity, O(n) space complexity

# Output
# Example:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]

"""
i = 0 1 2
start = 0, i = 0 -> swap index 0 itself [1,2,3]
    start = 1, i = 1 -> swap index 1 with 1 [1,2,3] (x)
        start = 2, i = 2 -> swap index 2 with 2 [1,2,3] (x)

    start = 1, i = 2 -> swap index 1 with 2 [1,3,2]
        start = 2, i = 2 -> swap index 2 with 2 [1,3,2] (x)

start = 0, i = 1 -> swap index 0 with 1 [2,1,3]
    start = 1, i = 1 -> swap index 1 with 1 [2,1,3] (x)
        start = 2, i = 2 -> swap index 2 with 2 [2,1,3] (x)

    start = 1, i = 2 -> swap index 1 with 2 [2,3,1]
        start = 2, i = 2 -> swap index 2 with 2 [2,3,1] (x)

start = 0, i = 2 -> swap index 0 with 2 [3,2,1]
    start = 1, i = 1 -> swap index 1 with 1 [3,2,1] (x)
        start = 2, i = 2 -> swap index 2 with 2 [3,2,1] (x)
        
    start = 1, i = 2 -> swap index 1 with 2 [3,1,2]
        start = 2, i = 2 -> swap index 2 with 2 [3,1,2] (x)

res = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
"""