class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if mapping.get(num, -1) != -1:
                return [mapping[num], i]
            else:
                mapping[remaining] = i
                
# O(n) time complexity, O(n) space complexity