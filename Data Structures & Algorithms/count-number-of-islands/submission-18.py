class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands=0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c]="0" #marked visited

            while queue:
                row,col = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]

                for dr,dc in directions:
                    nr = row+dr
                    nc = col+dc

                    if (0<=nr<rows or 0<=nc<cols or grid[nr][nc]=="1"):
                        queue.append((nr,nc))
                        grid[nr][nc]="0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    bfs(r,c)
        return islands