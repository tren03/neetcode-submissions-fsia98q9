class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> st;
        if(s.size()!=t.size()){
            return false;
        }
        for(auto i: s)
        {
            st[i]++;
        }

        for(auto i:t){
            if(st.find(i)==st.end())
            {
                return false;
                break;
            }else{
                int count = st[i];
                if(count==0){
                    return false;
                    break;
                }
                st[i]--;
                
            }

        
        }

        for(auto i:st){
            if(i.second!=0){
                return false;
            }
        }
        return true;
        
    }
};
