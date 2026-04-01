/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/


class Solution {
public:
    Node* dfs(Node* node,unordered_map<Node*,Node*> &mp)
    {       
        // if node already exists in hashmap, we need to return that instead of creating new node,
        // so we can connect other nodes to it in future

        if(mp.find(node)!= mp.end())
        {
            auto n = mp.find(node);
            return n->second;
        }

        //create new node
        Node* copy = new Node(node->val);

        // add new copy node to hashmap
        mp[node] = copy; // or mp.insert({node,copy});

        //make copy for every single neigh of node
        for(auto i : node->neighbors)
        {
            copy->neighbors.push_back(dfs(i,mp));
        }

        return copy;


        



    }
    Node* cloneGraph(Node* node) {
        unordered_map<Node*,Node*> mp;

        if(!node)
        {
            return nullptr;
        }

        return dfs(node,mp);


        
    }
};
