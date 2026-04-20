class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set() #r+c
        negDiag = set() #r-c
        board = [["."]*n for _ in range(len(n))]
        res = []
        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in negDiag:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                diag.add([row-col])
                negDiag.add([row+col])
                
                backtrack(row+1)

                board[row][col] = "."
                cols.remove(col)
                diag.remove([row-col])
                negDiag.remove([row+col])
        backtrack(0)
        return res

