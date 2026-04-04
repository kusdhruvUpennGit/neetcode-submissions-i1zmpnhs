class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #creating set
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    continue
                value = board[r][c]
                if value in rows[r] or value in cols[c] or value in squares[r//3,c//3]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                squares[r//3,c//3].add(value)
        
        return True