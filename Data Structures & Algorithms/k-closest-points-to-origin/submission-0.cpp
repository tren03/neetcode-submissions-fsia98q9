

using namespace std;

class Solution {
public:
    float dist(const vector<int>& p) {
        return sqrt(pow(p[0], 2) + pow(p[1], 2));
    }
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Max-heap to keep the k closest points
        priority_queue<pair<float, vector<int>>> p;
        
        for (const auto& point : points) {
            float d = dist(point);
            if (p.size() == k) {
                if (p.top().first > d) {
                    p.pop();
                    p.push({d, point});
                }
            } else {
                p.push({d, point});
            }
        }
        
        vector<vector<int>> ans;
        while (!p.empty()) {
            ans.push_back(p.top().second);
            p.pop();
        }
        
        return ans;
    }
};
