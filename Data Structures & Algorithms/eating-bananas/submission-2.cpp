#include<cmath>

class Solution {
public:
    int hours_taken(vector<int>& piles,int k)
    {
        int sum = 0;
        for(auto i:piles)
        {
            if(i<=k)
            {
                sum+=1;
            }
            else
            {
                
                double temp = ceil(i/(double)k);
                sum += int(temp);
                
            }
        }
        return sum;

    }
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(),piles.end());
        int l = 1;
        int r = piles[piles.size()-1];
        int ans;

        while(r>=l)
        {
            int mid = (l+r)/2;
            int h_taken = hours_taken(piles,mid);

            if(h_taken <= h)
            {
                ans = min(ans,mid);
                r = mid - 1;
            }
            else
            {
                l = mid+1;
            }

        }
        return ans;

        
    }
};
