class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {

        // form a adj matrix
        vector<vector<int>> adj(n,vector<int> {});
        for(auto i:edges){
            adj[i[1]].push_back(i[0]);
            adj[i[0]].push_back(i[1]);
        }
        for(auto i:adj){
            for(auto j:i){
                cout<<j; 
                }
                cout<<endl;

        }
        // not have many components
        // not have cycle

        // for componenets, do dfs, if all nodes not reached,then its a graph
        stack<int> st;
        vector<int>vis(n,0);
        vector<int> dfs_ans;

        st.push(0);
        while(!st.empty()){
            int temp = st.top();
            st.pop();
            vis[temp]=1;
            dfs_ans.push_back(temp);

            for(auto i:adj[temp]){
                if(vis[i]==0){
                    st.push(i);
                }
            }
            
        }

        if(dfs_ans.size()!=n){
            return false;
        }


        queue<pair<int,int>> q;// to store {node,parent}

        vector<int>visi(n,0);
        q.push({0,-1});

        visi[0]=1;
        while(!q.empty()){
            pair<int,int> temp = q.front();
            q.pop();

            for(auto i:adj[temp.first]){
                if(visi[i] == 1 && i!=temp.second){
                    return false;

                }
                if(visi[i] == 0){
                    q.push({i,temp.first});
                    visi[i]=1;
                }


            }
    
            
        }
        return true ;
    }
};



