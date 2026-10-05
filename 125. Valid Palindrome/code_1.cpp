class Solution {
public:
    bool isPalindrome(string s) {
        unordered_set<char> alnum;
        string valid_chars = {"abcdefghijklmnopqrstuvwxyz0123456789"};

        // Get alnum set
        for (auto& ch : valid_chars){
            alnum.insert(ch);
        }

        // print alnum
        // for (auto& ele : alnum){
        //     cout << ele;
        // }
        // cout << endl;

        string new_s = "";
        for (auto& ch : s){
            if (alnum.find(tolower(ch)) != alnum.end()){
                new_s += tolower(ch);
            }
        }
        // print new_s
        // for (auto& ele : new_s){
        //     cout << ele;
        // }
        // cout << endl;

        if (new_s.size() <= 1){
            return true;
        }

        int head = 0;
        int tail = new_s.size()-1;
        while (head < tail){
            if (new_s[head] != new_s[tail]){
                return false;
            } else {
                head++;
                tail--;
            }
        }

        return true;
    }
};

// O(n) time complexity, O(n) space complexity