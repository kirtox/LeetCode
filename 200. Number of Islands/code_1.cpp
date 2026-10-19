class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;

        for (int r=0 ; r<grid.size() ; r++){
            for (int c=0 ; c<grid[r].size() ; c++){
                if (grid[r][c] == '1'){
                    res++;
                    dfs(grid, r, c);
                }
            }
        }
        return res;
    }

    void dfs(vector<vector<char>>& grid, int r, int c){
        if (grid[r][c] == '1'){
            grid[r][c] = '0';
        } else {
            return;
        }

        // Up
        if (r > 0){
            dfs(grid, r - 1, c);
        }
        // Down
        if (r < grid.size() - 1){
            dfs(grid, r + 1, c);
        }
        // Left
        if (c > 0){
            dfs(grid, r, c - 1);
        }
        // Right
        if (c < grid[r].size() - 1){
            dfs(grid, r, c + 1);
        }
    }
};

// O(m * n) time complexity, O(m * n) space complexity (due to recursion stack)