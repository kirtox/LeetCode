class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0
        visited = set()

        while right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
                right += 1
            else:
                longest = max(longest, (right-1) - left + 1)
                visited.remove(s[left])
                left += 1
                
        longest = max(longest, (right-1) - left + 1)
        return longest

# O(n) time complexity, O(n) space complexity