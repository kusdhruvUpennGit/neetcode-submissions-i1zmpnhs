class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        maxArea = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c]=0 #mark visited
            area = 0
            while queue:
                area+=1
                row,col = queue.popleft()
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr,dc in directions:
                    nr,nc = dr+row,dc+col
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        queue.append((nr,nc))
                        grid[nr][nc]=0
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxArea = max(maxArea,bfs(r,c))
        return maxArea