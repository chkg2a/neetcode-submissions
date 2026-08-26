class Solution {
public:

string encode(vector<string> &strs) {
  string str = "";
  for (auto x : strs) {
    str.append(x);
    str.append("`");
  }
  return str;
}

vector<string> decode(string s) {
  vector<string> output;
  string a = "";
  for (auto x : s) {
    if (x == '`') {
      output.push_back(a);
      a = "";
      continue;
    }
    a += x;
  }
  return output;
}

};
