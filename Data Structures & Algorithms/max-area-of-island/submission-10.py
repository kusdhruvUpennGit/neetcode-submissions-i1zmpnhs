class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c]=0
            area = 1

            while queue:
                row,col = queue.popleft()
                area+=1
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if 0<=nr<rows and 0<=nc<=cols and grid[nr][nc]==1:
                        grid[nr][nc]=0
                        queue.append((nr,nc))
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxArea = max(maxArea,bfs(r,c))
        
        return maxArea