class Solution:
    def minRotations(self, s: str) -> int:
        # 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9
        # 9 -> 1: 8 or 2
        # 2 -> 8: 6 or 4

        prev = "0"
        rotations = 0
        for digit in s:
            if prev != digit:
                big = max(int(prev), int(digit))
                small = min(int(prev), int(digit))
                diff = big - small
                # print(min(diff, 10-diff), end="")
                rotations += min(diff, 10-diff)
                prev = digit

        # print()
        # print(f"rotations: {rotations}")
        return rotations

# O(n) time complexity, O(1) space complexity