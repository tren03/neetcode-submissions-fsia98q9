

using namespace std;

class Solution {
public:
    float dist(const vector<int>& p) {
        return sqrt(pow(p[0], 2) + pow(p[1], 2));
    }

    static bool comp(vector<int>p1,vector<int>p2)
    {
        return sqrt(pow(p1[0],2)+pow(p1[1],2))>sqrt(pow(p2[0],2)+pow(p2[1],2));
    }
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(),points.end(),comp);
        int temp = points.size()-1;
        vector<vector<int>> ans;
        for(int i=0;i<k;i++)
        {
            ans.push_back(points[temp]);
            temp--;
            
        }
        return ans;
    }
};
