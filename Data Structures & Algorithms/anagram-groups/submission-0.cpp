class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       vector<vector<string>> output;
  unordered_map<string,vector<string>> um;
  for(auto x : strs){
    string y = x;
    sort(x.begin(), x.end());
    um[x].push_back(y);
  }
  for(auto x : um){
    output.push_back(x.second);
  }
  return output;
   
    }
};
