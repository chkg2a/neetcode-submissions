class Solution {
public:
    int maxProfit(vector<int>& prices) {
           int low = 0;
    int high = 1;
    int profit = 0;
    while (high < prices.size()) {
      if (prices[high] < prices[low]) {
        low = high;
      }
      profit = max(profit, prices[high] - prices[low]);
      high++;
    }
    return profit;
 
    }
};
