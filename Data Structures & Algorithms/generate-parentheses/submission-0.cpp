class Solution {
public:
void backTrack(int n, int open, int close, vector<char> &output,
               vector<string> &results) {
  if (open == n && close == n) {
    string outString(output.begin(), output.end());
    results.push_back(outString);
  }
  if (open < n) {
    output.push_back('(');
    backTrack(n, open + 1, close, output, results);
    output.pop_back();
  }
  if (close < open) {
    output.push_back(')');
    backTrack(n, open, close + 1, output, results);
    output.pop_back();
  }
}

vector<string> generateParenthesis(int n) {
  vector<string> output;
  vector<char> result;
  backTrack(n, 0, 0, result, output);
  return output;
}

};
