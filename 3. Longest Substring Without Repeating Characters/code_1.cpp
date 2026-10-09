# include <unordered_set>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longest = 0;
        int left = 0;
        int right = 0;

        unordered_set<int> visited;

        while (right < s.size()){
            if (visited.find(s[right]) == visited.end()){
                visited.insert(s[right]);
                right++;
            } else {
                longest = max(longest, (right-1) - left + 1);
                visited.erase(s[left]);
                left++;
            }
        }
        longest = max(longest, (right-1) - left + 1);
        return longest;
        
    }
};

// O(n) time complexity, O(n) space complexity