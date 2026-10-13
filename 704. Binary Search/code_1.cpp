class Solution {
public:
    int search(vector<int>& nums, int target) {
        int mid = 0;
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right){
            mid = (left + right) / 2;

            if (target == nums[mid]){
                return mid;
            } else if (target < nums[mid]){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
};

// O(log n) time complexity, O(1) space complexity