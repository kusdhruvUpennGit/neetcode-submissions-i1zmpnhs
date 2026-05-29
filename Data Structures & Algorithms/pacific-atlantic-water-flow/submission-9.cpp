class Solution {
public:
    void dfs(vector<vector<int>>& heights, int r,int c,vector<vector<bool>>& visited){
        int rows = heights.size();
        int cols = heights[0].size();

        visited[r][c]=true;
        vector<pair<int,int>> directions = {{1,0},{-1,0},{0,1},{0,-1}};
        for(auto& dr: directions){
            int nr = r+dr.first;
            int nc = c+dc.second;

            if (nr<0 || nc<0 || nr>=rows || nc>=cols){
                continue;
            }
            if(visited[nr][nc]){
                continue;
            }
            if(heights[nr][nc]<heights[r][c]){
                continue;
            }
            dfs(heights,nr,nc,visited);
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if(heights.empty()||heights[0].empty()){
            return {};
        }
        int rows = heights.size();
        int cols = heights[0].size();

        vector<vector<bool>> pacific(rows,vector<bool>(cols,false));
        vector<vector<bool>> atlantic(rows,vector<bool>(cols,false));

        for(int c=0;c<cols;c++){
            if(!pacific[0][c]){
                dfs(heights,0,c,pacific);
            }
            if(!atlantic[rows-1][c]){
                dfs(heights,rows-1,c,atlantic);
            }
        }
        for(int r=0;r<rows;r++){
            if(!pacific[r][0]){
                dfs(heights,r,0,pacific);
            }
            if(!atlantic[r][cols-1]){
                dfs(heights,r,cols-1,atlantic);
            }
        }
        vector<vector<int>>result;
        for(int r=0;r<rows;r++){
            for (int c=0;c<cols;c++){
                if(pacific[r][c]&&atlantic[r][c]){
                    result.push_back({r,c});
                }
            }
        }
        return result;
    }
};
