class Solution {
public:
    bool isValid(string s) {
          stack<char> c;
  unordered_map<char, char> closeOpen = {{'}', '{'}, {')', '('}, {']', '['}};

  for(auto x : s){
    if(closeOpen.count(x)){
      if(!c.empty() && c.top() == closeOpen[x]){
        c.pop();
      }
      else{
        return false;
      }
    }
    else{
      c.push(x);
    }
  }
  if (c.empty()) {
    return true;
  } else {
    return false;
  }

    }
};
