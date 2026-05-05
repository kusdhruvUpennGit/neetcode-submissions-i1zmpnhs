class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        minutes = 0
        fresh=0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    rotten.append((r,c))
        
        while fresh>0 and rotten:
            for _ in range(len(rotten)):
                row,col = rotten.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc = col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        fresh-=1
                        rotten.append((nr,nc))
                        grid[nr][nc]=2
            minutes+=1
        if fresh==0:
            return minutes
        else:
            return -1
