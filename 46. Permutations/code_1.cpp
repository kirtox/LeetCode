class Solution {
private:
    vector<vector<int>> res;

public:
    vector<vector<int>> permute(vector<int>& nums) {
        backtracking(0, nums);
        return res;
    }

    void backtracking(int start, vector<int>& nums){
        if (start == nums.size()){
            res.push_back(nums);
            return;
        }

        for (int i=start ; i<nums.size() ; i++){
            int tmp = nums[start];
            nums[start] = nums[i];
            nums[i] = tmp;

            backtracking(start + 1, nums);

            tmp = nums[start];
            nums[start] = nums[i];
            nums[i] = tmp;
        }
    }
};

// O(n! * n) time complexity, O(n) space complexity