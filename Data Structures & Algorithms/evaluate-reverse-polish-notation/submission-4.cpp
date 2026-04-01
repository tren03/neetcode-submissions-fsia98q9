
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(auto itr:tokens)
        {   
            char i = itr[0];

            if((i == '+' || i=='-'|| i=='*'||i=='/') && itr.size()==1)
            {
                int res = 0;
                int a1 = st.top();
                st.pop();
                int b1 = st.top();
                st.pop();
                    
                if(i=='+')
                {
                    res=b1+a1;                    
                }
                if(i=='-')
                {
                    res=b1-a1;                    
                }
                if(i=='*')
                {
                    res=b1*a1;                    
                }
                if(i=='/')
                {
                    res=b1/a1;                    
                }
                cout<<res<<endl;
                st.push(res);
                
            }
            else
            {
                st.push(stoi(itr));      
                 
            }
        }
        
        
        return st.top();
        
    }
};
