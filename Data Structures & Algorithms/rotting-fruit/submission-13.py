class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        rotten = deque()
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    rotten.append((r,c))
        directions = [(1,0),(0,-1),(-1,0),(0,1)]

        while rotten and fresh>0:
            for _ in range(len(rotten)):
                row,col = rotten.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        fresh-=1
                        rotten.append((nr,nc))
            time+=1
        
        if fresh==0:
            return minutes
        else:
            return -1