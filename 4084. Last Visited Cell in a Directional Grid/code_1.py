class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        len_r = len(grid)
        len_c = len(grid[0])

        visited = set()

        curr_r = 0
        curr_c = 0
        visited.add(tuple([curr_r, curr_c]))

        while True:
            prev_r, prev_c = curr_r, curr_c
            # Check border, then move
            if grid[curr_r][curr_c] == "R" and curr_c < len_c - 1:
                curr_c += 1
                # print(f"R -> ({curr_r}, {curr_c})")
            elif grid[curr_r][curr_c] == "L" and curr_c >= 0 + 1:
                curr_c -= 1
                # print(f"L -> ({curr_r}, {curr_c})")
            elif grid[curr_r][curr_c] == "D" and curr_r < len_r - 1:
                curr_r += 1
                # print(f"D -> ({curr_r}, {curr_c})")
            elif grid[curr_r][curr_c] == "U" and curr_r >= 0 + 1:
                curr_r -= 1
                # print(f"U -> ({curr_r}, {curr_c})")
            else:
                # print(f"Out of border (? -> return [{prev_r}, {prev_c}]")
                return [prev_r, prev_c]

            # Check if node is visited
            if (curr_r, curr_c) in visited:
                # print(f"Already visited -> [{curr_r}, {curr_c}], return [{prev_r}, {prev_c}]")
                return [prev_r, prev_c]
            else:
                visited.add(tuple([curr_r, curr_c]))
                # print(f"Not visited -> [{curr_r}, {curr_c}], add into visited {visited}")
                
                
# O(m * n) time complexity, O(m * n) space complexity, where m is the number of rows and n is the number of columns