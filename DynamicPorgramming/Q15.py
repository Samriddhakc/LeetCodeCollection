class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        # 0 1  => 3    => 0 1
        # 1 1       1 1

        n, m = len(matrix), len(matrix[0])

        cache = {}

        # Big O(n * m) time | O( min(n, m) ) space.

        def _countSquares(x, y, size=1):

            if x >= n or y >= m:
                return 0

            if matrix[x][y] == 0:
                return 0

            if (x, y) in cache:
                return cache[(x, y)]

            dwn = _countSquares(x, y + 1, size + 1)
            diag = _countSquares(x + 1, y + 1, size + 1)
            side = _countSquares(x + 1, y, size + 1)
            cache[(x, y)] = 1 + min(dwn, diag, side)

            return cache[(x, y)]

        total_count = 0

        # print(_countSquares(0, 0))
        # print(_countSquares(0, 1))
        # print(_countSquares(1, 1))
        # print(_countSquares(1, 0))

        for i in range(n):
            for j in range(m):
                # print(i, j)
                total_count += _countSquares(i, j)

        return total_count