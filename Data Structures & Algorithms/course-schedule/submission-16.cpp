class Solution {
public:
    bool dfs(int course, vector<vector<int>>& graph, vector<int>& state){
        if(state[course]==1){
            return false;
        }

        if(state[course]==2){
            return true;
        }

        state[course]=1;

        for(int prereq: graph[course]){
            if(!dfs(prereq,graph,state)){
                return false;
            }
        }
        state[course]=2;
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);

        for(auto& edge:prerequisites){
            int course = edge[0];
            int prereq = edge[1];
            graph[course].push_back(prereq);
        }

        vector<int> state(numCourses,0);
        for(int course=0; course<numCourses;course++){
            if(!dfs(course,graph,state)){
                return false;
            }
        }
        return true;
    }
};
