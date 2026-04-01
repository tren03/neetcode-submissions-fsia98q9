class Solution {
public:

    string encode(vector<string>& strs) {
        string cipher = "";
        for(auto itr:strs)
        {
            string temp = itr;
            temp+=";;";
            cipher+=temp;
        }
        cout<<cipher;
        return cipher;
        


    }

    vector<string> decode(string s) {
        vector<string> ans;
        string temp = "";
        if(s.size()==0)
        {
            return ans;
        }
        for(int i=0;i<s.size()-1;i++)
        {
            
            if(s[i]==';' && s[i+1]==';')
            {
                ans.push_back(temp);
                temp = "";
                i+=1;
            }
            else
            {
                temp+=s[i];
            }
            
        }
        return ans;

    }
};
