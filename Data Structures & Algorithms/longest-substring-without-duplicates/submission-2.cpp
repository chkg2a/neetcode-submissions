class Solution {
public:
    int lengthOfLongestSubstring(string s) {
      unordered_set<char> set;
      if (s.size() < 1) return 1;
      int left = 0;
      int right = 0;
      int maxS = 1;

      while (right < s.size()){
        while (set.count(s[right])){
          set.erase(s[left]);
          left++;
        }
        set.insert(s[right]);
        right++;
        maxS = max(maxS,right - left);
      }
      return maxS;

    }
};
