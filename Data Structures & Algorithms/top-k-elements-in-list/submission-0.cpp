class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
         vector<int> output;
  unordered_map<int, int> numMap;
  vector<pair<int, int>> ns;

  for (auto x : nums) {
    numMap[x]++;
  }

  for (auto x : numMap) {
    ns.push_back(make_pair(x.second, x.first));
  }
  sort(ns.rbegin(), ns.rend());
  int i = 0;
  for (auto x : ns) {
    i++;
    output.push_back(x.second);
    if (i == k) {
      return output;
    }
  }
  return output;
 
    }
};
