class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        nrows, ncols = len(heights), len(heights[0])

        def dfs(dfs_stack):

            '''
            :return:
            '''
            can_reach = set()

            while dfs_stack:

                c_x, c_y = dfs_stack.pop()
                can_reach.add((c_x, c_y))

                for (d_x, d_y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

                    n_x, n_y = c_x + d_x, c_y + d_y

                    # avoid cycle 
                    if (n_x, n_y) in can_reach:
                        continue

                        # check for bounds.
                    if n_x >= nrows or n_x < 0 or n_y >= ncols or n_y < 0:
                        continue

                    # continue if it breaks/violates the bound
                    if heights[n_x][n_y] < heights[c_x][c_y]:
                        continue

                    dfs_stack.add((n_x, n_y))

            return can_reach

        pacific_cords = set()
        atlantic_cords = set()

        for col in range(ncols):
            pacific_cords.add((0, col))
            atlantic_cords.add((nrows - 1, col))

        for row in range(nrows):
            pacific_cords.add((row, 0))
            atlantic_cords.add((row, ncols - 1))

        all_pacific_cords = dfs(pacific_cords)
        all_atlantic_cords = dfs(atlantic_cords)

        return all_pacific_cords.intersection(all_atlantic_cords)
