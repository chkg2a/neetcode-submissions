class Solution {
public:
    int lengthOfLongestSubstring(string s) {
      int left = 0;
      int right = 1;
      int maxS = 0;
      while (right < s.size()){
        if(s[left] == s[right]){
          left++;
        }else{
          right++;
        }
        maxS = max(maxS,right - left);
      }
      return maxS;

    }
};
