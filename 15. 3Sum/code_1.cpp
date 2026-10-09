class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> triplets = {};
        sort(nums.begin(), nums.end());

        for (int i=0 ; i<nums.size() ; i++){
            // Pass repeat
            if (i > 0 and nums[i] == nums[i-1]){
                continue;
            }

            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right){
                int total = nums[i] + nums[left] + nums[right];

                if (total == 0){
                    triplets.push_back({nums[i], nums[left], nums[right]});

                    int curr_left = nums[left];
                    int curr_right = nums[right];
                    // Pass repeat
                    while (left < right and nums[left] == curr_left){
                        left++;
                    }
                    while (left < right and nums[right] == curr_right){
                        right--;
                    }

                } else if (total < 0){
                    left++;
                } else {
                    right--;
                }
            }
        }

        return triplets;
    }
};


// O(n^2) time complexity, O(n) space complexity