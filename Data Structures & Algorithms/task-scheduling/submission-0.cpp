class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int> mp;
        priority_queue<int> p; // default is max heap

        for(auto i:tasks)
        {
            mp[i]++;
        }

        for(auto i:mp)
        {
            p.push(i.second);
        }

        int time = 0;
        queue<pair<int,int>> q;
        while(!q.empty() || !p.empty())
        {
            time++;
            if(!q.empty() && q.front().second <= time)
            {
                int temp = q.front().first;
                q.pop();
                p.push(temp);
            }
            
            if(!p.empty())
            {
                int temp = p.top();
                p.pop();
                temp--;
                if(temp>0)
                {
                    q.push({temp,time+n+1});
                }
            }
            
        }
        return time;
        

         

        
    }
};
