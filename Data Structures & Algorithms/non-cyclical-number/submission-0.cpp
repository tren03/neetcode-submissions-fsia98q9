class Solution {
public:
    unordered_set<int> st;
    bool isHappy(int n) {
        int sum=0;
        while(1)
        {
            if(n==1)
            {
                return true;
            }
 
   
            sum =0;
            int temp=n;
            while(temp!=0)
            {
                int d= temp%10;
                sum+=pow(d,2);
                temp=temp/10;
            }
            cout<<sum;
            cout<<endl;
            if(st.find(sum)!=st.end())
            {
                return false;
            }
            st.insert(sum);
            n = sum;


                


           
        
        }

    }
};
