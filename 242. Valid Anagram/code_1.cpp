#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }

        unordered_map <char, int> umap;

        for (char c : s){
            if (umap.find(c) == umap.end()){
                umap[c] = 1;
            } else {
                umap[c] += 1;
            }
        }

        for (char c : t){
            if (umap.find(c) == umap.end()){
                return false;
            } else {
                if (umap[c] == 0){
                    return false;
                }
                umap[c] -= 1;
            }
        }

        return true;
    }
};

// O(n) time complexity, O(n) space complexity