class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # trie with dfs
        # hasset with dfs?

        # use backtracking

        n, m = len(board), len(board[0])

        def backtrack(row, col, suffix):

            '''
            Function to check all possibilities that make up the word
            '''

            if len(suffix) == 0:
                return True

            if row >= n or col >= m or row < 0 or col < 0:
                return False

            if board[row][col] == "#":
                return False

            if board[row][col] != suffix[0]:
                return False

            board[row][col] = "#"  # mark as visited.

            for r_delta, c_delta in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

                ret_val = backtrack(row + r_delta, col + c_delta, suffix[1:])

                if ret_val:
                    break

            board[row][col] = suffix[0]
            return True if ret_val else False

        for r in range(n):
            for c in range(m):
                if backtrack(r, c, word):
                    return True
        return False




