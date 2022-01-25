class Solution:
    def numIslands( self, grid ):

        if not grid or not grid[0]:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])

        def dfs(c_x, c_y, ):

            grid[c_x][c_y] = "0"  # mark it as visited

            for (d_x, d_y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                n_x, n_y = c_x + d_x, c_y + d_y

                if n_x >= n_rows or n_x < 0 or n_y >= n_cols or n_y < 0:
                    continue

                if grid[n_x][n_y] == "0":
                    continue

                dfs(n_x, n_y)

        total_islands = 0
        for c_x in range(n_rows):
            for c_y in range(n_cols):
                if grid[c_x][c_y] == "1":
                    total_islands += 1
                    dfs(c_x, c_y)

        return total_islands
