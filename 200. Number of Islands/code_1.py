class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            # up
            if i-1 >= 0:
                if grid[i-1][j] == "1":
                    grid[i-1][j] = "0"
                    dfs(i-1, j)
            # down
            if i+1 < len(grid):
                if grid[i+1][j] == "1":
                    grid[i+1][j] = "0"
                    dfs(i+1, j)
            # left
            if j-1 >= 0:
                if grid[i][j-1] == "1":
                    grid[i][j-1] = "0"
                    dfs(i, j-1)

            # right
            if j+1 < len(grid[0]):
                if grid[i][j+1] == "1":
                    grid[i][j+1] = "0"
                    dfs(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    count += 1
                    dfs(i, j)

        return count