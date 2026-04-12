class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preReq[crs].append(pre)
        
        visiting = set()
        visited = set()
        result=[]

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            result.append(crs)
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result