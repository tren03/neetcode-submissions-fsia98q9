class MinStack {
public:
    stack<int> st;
    stack<int> min;
    MinStack() {
        
        
        
    }
    
    void push(int val) {
        if(!min.empty())
        {
            if(val<min.top())
            {
                min.push(val);
            }
            else
            {
                min.push(min.top());
            }
        }
        else
        {
            min.push(val);
        }

        st.push(val);
        
    }
    
    void pop() {
        st.pop();
        min.pop();
        
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return min.top();


        
    }
};
