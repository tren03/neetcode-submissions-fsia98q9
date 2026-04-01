class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int min_val = prices[0];
       int temp = 0;
       int r= 0;
       int ans = 0;
       while(r<prices.size())
       {
            
            temp = prices[r]-min_val;
            ans = max(ans,temp); 
            if(prices[r]<min_val){
                ans = max(ans,temp);
                temp = 0;
                min_val = prices[r];
                
            }
            r++;
       }
       return ans;
    }
};
