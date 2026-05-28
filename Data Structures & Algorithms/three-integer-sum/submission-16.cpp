class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;  // Stores unique triplets
        sort(nums.begin(), nums.end());  // Sort for two-pointer approach

        int n = nums.size();

        // Only go until n - 2, because we need at least 2 elements after i
        for (int i = 0; i < n - 2; i++) {
            // Skip duplicate fixed values
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;      // Left pointer
            int right = n - 1;     // Right pointer

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum < 0) {
                    left++;  // Need a larger sum
                } 
                else if (sum > 0) {
                    right--; // Need a smaller sum
                } 
                else {
                    result.push_back({nums[i], nums[left], nums[right]});

                    left++;
                    right--;

                    // Skip duplicates safely
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }
            }
        }

        return result;
    }
};
