class Solution {
public:
  unordered_map<int,int> ns;

  for(int i = 0; i < nums.size(); i++){
    if(ns.count(target - nums[i])){
      return {ns[target - nums[i]], i};
    }
    ns[nums[i]] = i;
  }

  return {};

};
