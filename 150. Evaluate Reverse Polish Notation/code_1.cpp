#include <unordered_set>
#include <vector>
#include <string>

using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        unordered_set<string> op = {"+", "-", "*", "/"};
        vector<int> stack = {};

        for(auto& token : tokens){
            if (op.find(token) == op.end()){
                stack.push_back(stoi(token));
            } else {
                int num2 = stack[stack.size()-1];
                stack.pop_back();
                int num1 = stack[stack.size()-1];
                stack.pop_back();

                if (token == "+"){
                    stack.push_back(num1 + num2);
                } else if (token == "-"){
                    stack.push_back(num1 - num2);
                } else if (token == "*"){
                    stack.push_back(num1 * num2);
                } else if (token == "/"){
                    stack.push_back(num1 / num2);
                }
            }
        }
        return stack[0];
    }
};

// O(n) time complexity, O(n) space complexity