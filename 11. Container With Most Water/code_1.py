class Solution:
    def maxArea(self, height: list[int]) -> int:
        container = 0

        left = 0
        right = len(height) - 1

        while left < right:
            container = max(container, (right - left) * min(height[left], height[right]))

            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return container

# O(n) time complexity, O(1) space complexity