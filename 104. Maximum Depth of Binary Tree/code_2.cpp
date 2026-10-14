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
        if (root == nullptr){
            return 0;
        }
        
        int res = 0;
        vector<pair<TreeNode*, int>> stack;
        pair<TreeNode*, int> node = {root, 1};
        stack.push_back(node);

        while (!stack.empty()){
            node = stack[stack.size()-1];
            stack.pop_back();
            TreeNode* curr;
            int depth;
            curr = node.first;
            depth = node.second;
            res = max(res, depth);

            if (curr->left != nullptr){
                node.first = curr->left;
                node.second = depth + 1;
                stack.push_back(node);
            }
            if (curr->right != nullptr){
                node.first = curr->right;
                node.second = depth + 1;
                stack.push_back(node);
            }
        }
        return res;

    }
};

// O(n) time complexity, O(n) space complexity