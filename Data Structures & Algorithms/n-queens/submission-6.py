class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()      # row + col
        negDiag = set()   # row - col
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in diag or (row - col) in negDiag:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag.add(row + col)
                negDiag.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag.remove(row + col)
                negDiag.remove(row - col)

        backtrack(0)
        return res
