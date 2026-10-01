#include <unordered_map>
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> map;
        vector<int> res;
        // vector<int> res(2);

        for (int i=0 ; i<nums.size() ; i++){
            if (map.find(nums[i]) != map.end()){
                res.push_back(map[nums[i]]);
                res.push_back(i);
                break;
            }
            map[target - nums[i]] = i;
        }
        return res;
    }
};

// O(n) time complexity, O(n) space complexity