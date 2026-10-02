#include <unordered_map>
#include <map>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> umap;
        vector<vector<string>> res;

        for (int i=0; i<strs.size(); i++){
            map<char, int> curr_map;
            for (int j=0; j<strs[i].size(); j++){
                if(curr_map.find(strs[i][j]) == curr_map.end()){
                    curr_map[strs[i][j]] = 1;
                } else {
                    curr_map[strs[i][j]]++;
                }
            }
            string key = "";
            for (auto& pair : curr_map){
                char k = pair.first;
                int v = pair.second;
                key += to_string(v)+k;
            }

            if (umap.find(key) == umap.end()){
                umap[key] = {strs[i]};
            } else {
                umap[key].push_back(strs[i]);
            }

            
        }

        for (auto& pair : umap){
            vector<string> val = pair.second;
            res.push_back(val);
        }

        return res;
    }
};

// O(n * m) time complexity, O(n * m) space complexity