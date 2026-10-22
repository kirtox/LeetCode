class Solution {
private:
    int left = 0;
    int right = 0;
    vector<string> res;
    string curr = "";
    int n = 0;
public:
    vector<string> generateParenthesis(int n) {
        this->n = n;
        backtracking(curr, left, right);
        return res;
    }

    void backtracking(string curr, int left, int right){
        if (left == this->n && right == this->n){
            res.push_back(curr);
            return;
        }
        if (left > right){
            backtracking(curr + ")", left, right + 1);
        }
        if (left < n){
            backtracking(curr + "(", left + 1, right);
        }
    }
};

// O(4^n / sqrt(n)) time complexity, O(n) space complexity