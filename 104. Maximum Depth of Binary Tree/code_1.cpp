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
    int maxDepth(TreeNode* root) {
        
        int res = 0;
        vector<unordered_map<TreeNode*, int>> stack;
        unordered_map<TreeNode*, int> node;
        node[root] = 1;
        stack.push_back(node);

        while (!stack.empty()){
            node = stack[stack.size()-1];
            stack.pop_back();
            TreeNode* curr;
            int depth;
            for (auto& [k, v] : node){
                curr = k;
                depth = v;
            }
            res = max(res, depth);

            if (curr->left != nullptr){
                node.clear();
                node[curr->left] = depth + 1;
                stack.push_back(node);
            }
            if (curr->right != nullptr){
                node.clear();
                node[curr->right] = depth + 1;
                stack.push_back(node);
            }
        }
        return res;

    }
};

// O(n) time complexity, O(n) space complexity