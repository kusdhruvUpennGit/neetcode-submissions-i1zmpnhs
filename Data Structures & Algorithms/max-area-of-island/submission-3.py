class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c]==0:
                return 0
            
            visited.add((r,c))
            area = 1
            area+=dfs(r+1,c)
            area+=dfs(r,c+1)
            area+=dfs(r-1,c)
            area+=dfs(r,c-1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and(r,c) not in visited:
                    max_area = max(max_area,dfs(r,c))
        
        return max_area