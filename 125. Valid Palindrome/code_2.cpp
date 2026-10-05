class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() == 0){
            return true;
        }

        int head = 0;
        int tail = s.size()-1;
        
        while (head <= tail){
            while (head < tail && !isalnum(s[head])){
                head++;
            }
            while (head < tail && !isalnum(s[tail])){
                tail--;
            }
            if (tolower(s[head]) != tolower(s[tail])){
                return false;
            } else {
                head++;
                tail--;
            }
        }
        return true;
    }
};

// O(n) time complexity, O(1) space complexity