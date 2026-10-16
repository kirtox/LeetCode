class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
            else:
                return
            # up
            if r > 0:
                dfs(r - 1, c)
            # down
            if r < len(grid) - 1:
                dfs(r + 1, c)
            # left
            if c > 0:
                dfs(r, c - 1)
            # right
            if c < len(grid[r]) - 1:
                dfs(r, c + 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res

# O(m * n) time complexity, O(m * n) space complexity (due to recursion stack)