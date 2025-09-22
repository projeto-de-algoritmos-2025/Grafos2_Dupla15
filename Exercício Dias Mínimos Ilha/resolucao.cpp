class Solution {
public:
    int n, m;
    vector<int> dir = {0,1,0,-1,0};
    
    void dfs(vector<vector<int>>& grid, int i, int j, vector<vector<int>>& vis) {
        vis[i][j] = 1;
        for (int d = 0; d < 4; d++) {
            int x = i + dir[d], y = j + dir[d+1];
            if (x >= 0 && x < n && y >= 0 && y < m && 
                !vis[x][y] && grid[x][y] == 1) {
                dfs(grid, x, y, vis);
            }
        }
    }
    
    int count_islands(vector<vector<int>>& grid) {
        vector<vector<int>> vis(n, vector<int>(m, 0));
        int islands = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!vis[i][j] && grid[i][j] == 1) {
                    islands++;
                    dfs(grid, i, j, vis);
                }
            }
        }
        return islands;
    }
    
    int minDays(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        
        if (count_islands(grid) != 1) return 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    if (count_islands(grid) != 1) return 1;
                    grid[i][j] = 1;
                }
            }
        }
        
        return 2;
    }
};