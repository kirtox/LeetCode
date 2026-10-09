class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int buy = 0;
        int sell = 1;

        while (sell < prices.size()){
            if (prices[buy] > prices[sell]){
                buy = sell;
                sell++;
            } else {
                profit = max(profit, prices[sell] - prices[buy]);
                sell++;
            }
        }
        return profit;
    }
};

// O(n) time complexity, O(1) space complexity