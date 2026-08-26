class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
  vector<int> output;
  vector<int> prefixArr;
  vector<int> postfixArr;

  int prefix = 1;
  int postfix = 1;

  prefixArr.push_back(prefix);
  for(int i = 0; i < nums.size(); i++){
    prefix *= nums[i];
    prefixArr.push_back(prefix);
  }

  postfixArr.push_back(postfix);
  for(int i = nums.size()-1; i >= 0; i--){
    postfix *= nums[i];
    postfixArr.push_back(postfix);
  }
  
  std::reverse(postfixArr.begin(),postfixArr.end());
  for(int i = 0; i < nums.size(); i++){
    output.push_back(prefixArr[i] * postfixArr[i+1]);
  }

  return output;

    }
};
