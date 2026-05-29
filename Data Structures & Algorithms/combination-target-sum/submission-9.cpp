class Solution {
public:
    void dfs(int index, vector<int>& nums, int target, vector<int>& path, vector<vector<int>>& result){
        if (target==0){
            result.push_back(path);
            return;
        }

        if (target<0||index==nums.size()){
            return;
        }

        path.push_back(nums[index]);
        dfs(index,nums,target-nums[index], path, result);
        path.pop_back();

        dfs(index+1, nums, target, path, result);
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        vector<int> path;

        dfs(0, nums, target, path, result);

        return result;    
    }
};
