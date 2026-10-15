/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr){
            return {};
        }
        map<int, vector<int>> level_map;
        pair<TreeNode*, int> curr;
        vector<pair<TreeNode*, int>> stack = {{root, 1}};
        TreeNode* node;
        int depth;

        while (!stack.empty()){
            curr = stack[stack.size() - 1];
            stack.pop_back();
            node = curr.first;
            depth = curr.second;

            // Stored
            if (level_map.find(depth) != level_map.end()){
                level_map[depth].push_back(node->val);
            } else {
                vector<int> tmp;
                tmp.push_back(node->val);
                level_map[depth] = tmp;
            }

            if (node->right){
                curr.first = node->right;
                curr.second = depth + 1;
                stack.push_back(curr);
            }
            if (node->left){
                curr.first = node->left;
                curr.second = depth + 1;
                stack.push_back(curr);
            }
        }

        vector<vector<int>> res;

        for (auto& [k, v] : level_map){
            res.push_back(v);
        }
        return res;
    }
};

// O(n log h) time complexity, O(n) space complexity