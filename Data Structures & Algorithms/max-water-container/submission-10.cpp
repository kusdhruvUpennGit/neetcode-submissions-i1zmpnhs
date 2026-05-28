class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size()-1;
        int bestArea = 0;

        while (left<right){
            int width = right-left;
            int curHeight = min(heights[left],heights[right]);
            int currArea = width *curHeight;
            bestArea = max(bestArea,currArea);

            if (heights[left]<heights[right]){
                left++;
            }
            else{
                right--;
            }
        }

        return bestArea;
    }
};
