class Solution {
public:

    bool check(unordered_map<char,int> &sub,unordered_map<char,int> &mp)
    {
        if(sub==mp)
        {
            return true;
        }
        return false;
    }
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> sub;
        unordered_map<char,int> mp;

        for(auto i:s1)
        {
            sub[i]++;
        }
        int temp = 0;
        while(temp<s1.size())
        {
            mp[s2[temp]]++;
            temp++;
        }
        if(check(mp,sub))
        {
            return true;
        }
        for(auto i:mp)
            {
                cout<<i.first<<'\t'<<i.second<<endl;
            }
        cout<<endl<<endl;

        int l = 0;
        int r = s1.size()-1;

        mp[s2[l]]--;
            if(mp[s2[l]]==0)
            {
                mp.erase(mp.find(s2[l]));
            }
            l++; 
            r++;   
        mp[s2[r]]++;        
        
        for(auto i:mp)
            {
                cout<<i.first<<'\t'<<i.second<<endl;
            }
        cout<<endl<<endl;

        

        
        while(r<s2.size())
        {
            if(check(mp,sub))
            {
                return true;
            }
            mp[s2[l]]--;
            if(mp[s2[l]]==0)
            {
                mp.erase(mp.find(s2[l]));
            }
            l++; 
            r++;   
            mp[s2[r]]++;

            if(check(mp,sub))
            {
                return true;
            }
            for(auto i:mp)
            {
                cout<<i.first<<'\t'<<i.second<<endl;
            }
            cout<<endl<<endl;
            

        }
        return false;

        
        

        
    }
};
