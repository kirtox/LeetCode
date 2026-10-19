class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        left = 0
        right = 0
        res = []
        curr = ""

        def backtracking(curr: str, left: int, right: int):
            # print(f"('{curr}', {left}, {right})")
            
            if left == n and right == n:
                res.append(curr)

            if left < n:
                backtracking(curr + "(", left + 1, right)

            if right < n and right < left:
                backtracking(curr + ")", left, right + 1)

        backtracking(curr, left, right)

        # print(f"res: {res}")
        return res

# O(n * 4^n / sqrt(n)) time complexity, O(n) space complexity