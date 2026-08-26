class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
  vector<vector<string>> output;
  unordered_map<string,vector<string>> numMap;

  for(auto x : strs){
    string str = x;
    sort(x.begin(),x.end());
    numMap[x].push_back(str);
  }

  for(auto x : numMap){
    output.push_back(x.second);
  }
  
  return output;
    }
};
