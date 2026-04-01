class KthLargest {
public:
    priority_queue<int,vector<int>,greater<int>> p;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(auto itr:nums)
        {
            if(p.size()==k)
            {
                if(itr>p.top())
                {
                    p.pop();
                    p.push(itr);
                }
            }
            else
            {
                p.push(itr);
            }
            
        }
        
        
        
    }
    
    int add(int val) {
        if(p.size()==k)
        {
            if(val>p.top())
            {
                p.pop();
                p.push(val);
            }
        }
        else
        {
                p.push(val);
        }

        return p.top();
        
        
    }
};
