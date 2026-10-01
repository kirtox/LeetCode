#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set <int> num_set;

        for (int i=0 ; i<nums.size() ; i++){
            if (num_set.find(nums[i]) != num_set.end()){
                return true;
            } else {
                num_set.insert(nums[i]);
            }
        }
        return false;
    }
};

// O(n) time complexity, O(n) space complexity
// Using unordered_set instead of unordered_map to store unique elements, which is more appropriate for this problem.