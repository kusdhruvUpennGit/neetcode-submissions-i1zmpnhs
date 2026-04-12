class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        q = deque()
        directions = [(1,0),(0,1),(0,-1),(-1,0)]

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return
            visited.add((r,c))
            q.append((r,c))

            for dr,dc in directions:
                dfs(r+dr,c+dc)
        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    found=True
                    break
        steps=0

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if grid[nr][nc]==1:
                            return steps
                        visited.add((nr,nc))
                        q.append((nr,nc))
            steps+=1