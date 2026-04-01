class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for (auto i : nums) {
            mp[i]++;
        }

        // Priority queue to store pairs (frequency, number)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        for (auto i : mp) {
            if (pq.size() < k) {
                pq.push({i.second, i.first}); // Store frequency and number
            } else {
                if (i.second > pq.top().first) {
                    pq.pop();
                    pq.push({i.second, i.first});
                }
            }
        }

        vector<int> ans;
        while (!pq.empty()) {
            ans.push_back(pq.top().second); // Push back the number
            pq.pop();
        }

        return ans;
    }
};
