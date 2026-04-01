class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int,vector<int>> maxheap;
        for(auto i:stones)
        {
            maxheap.push(i);
        }
        while(maxheap.size()>=2)
        {
            int x = maxheap.top();
            maxheap.pop();
            int y = maxheap.top();
            maxheap.pop();

            if(x>y)
            {
                maxheap.push(x-y);
            }
            else if(y>x)
            {
                maxheap.push(y-x);
            }
        }

        if(maxheap.size()==0)
        {
            return 0;
        }
        else
        {
            return maxheap.top();
        }

        
    }
};
