class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDia = set()
        negDia = set()
        result = []
        board = [["."]*n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append("".join(r) for r in board)
                return
            for col in range(n):
                if col in cols or (row+col) in posDia or (row-col) in negDia:
                    continue
                
                board[row][col]="Q"
                cols.add(col)
                posDia.add(row+col)
                negDia.add(row-col)

                backtrack(row+1)

                board[row][col]="."
                cols.remove(col)
                posDia.remove(row+col)
                negDia.remove(row-col)
        backtrack(0)
        return result