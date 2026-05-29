class Solution {
public:
    int rob(vector<int>& nums) {
        // dp[i]=max(dp[i-1],nums[i]+dp[i-2])

        int prev1 = 0;
        int prev2 = 0;

        for(int money : nums){
            int take = money+prev2;
            int skip = prev1;
            int current = max(take,skip);

            prev2=prev1;
            prev1 = current;
        }
        return prev1;
    }

};
