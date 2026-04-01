class Solution {
public:


    bool Ana(string s,string t){
        unordered_map<int,int> mp;

        if(s.size()!=t.size()){
            return false;
        }
        for(auto i:s){
            mp[i]++;
        }

        for(auto i:t){
            if(mp.find(i)==mp.end()){
                return false;
            }else if(mp[i]==0){
                return false;
            }
            mp[i]--;
        }

        for(auto i:mp){
            if(i.second!=0){
                return false;
            }
        }
        return true;
    }

    vector<string> getAna(string s, vector<string> &str){
        vector<string> anaList;
        int i=0;
        while(i<str.size()){
            if(Ana(str[i],s)){
                anaList.push_back(str[i]);
                str.erase(str.begin()+i);
            }else{
                i++;
            }
        }

        return anaList;

        
        

    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        while(strs.size()!=0){
            ans.push_back(getAna(strs[0],strs));
        }

        return ans;


        
    }
};
