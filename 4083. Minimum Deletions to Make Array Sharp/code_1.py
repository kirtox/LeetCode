class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        first = 0
        second = 1
        res = 0
        
        while first < len(nums) - 1:
            if nums[first] ^ nums[second] == 0:
                res += 1

            first, second = second, second + 1

        return res

# O(n) time complexity, O(1) space complexity