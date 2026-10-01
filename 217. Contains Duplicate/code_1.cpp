#include <unordered_map>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map <int, int> num_set;

        for (int i=0 ; i<nums.size() ; i++){
            if (num_set.find(nums[i]) != num_set.end()){
                return true;
            } else {
                num_set[nums[i]] = 1;
            }
        }
        return false;
    }
};

// O(n) time complexity, O(n) space complexity