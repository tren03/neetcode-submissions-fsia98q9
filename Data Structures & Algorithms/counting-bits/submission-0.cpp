class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans;
        for(int i=0;i<=n;i++){
            int temp=i;
            int temp_ones = 0;
            while(temp){
                if(temp%2==1){
                    temp_ones++;
                }
                temp=temp>>1;
            }
            ans.push_back(temp_ones);
        }
        return ans;

        
    }
};
