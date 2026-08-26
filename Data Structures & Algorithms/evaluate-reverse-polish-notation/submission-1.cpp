class Solution {
public:
int evalRPN(vector<string> &tokens) {
  stack<int> stk;
  double op1, op2, value;
  for (auto x : tokens) {
    if ((x[0] == '+' || x[0] == '-' || x[0] == '*' || x[0] == '/') &&
        x[1] == '\0') {
      op2 = stk.top();
      stk.pop();
      op1 = stk.top();
      stk.pop();
      switch (x[0]) {
      case '+':
        value = op1 + op2;
        break;
      case '-':
        value = op1 - op2;
        break;
      case '*':
        value = op1 * op2;
        break;
      case '/':
        value = op1 / op2;
        break;
      }
      stk.push(value);
    } else {
      int num;
      stringstream ss(x);
      while (ss >> num) {
        stk.push(num);
      }
    }
  }
  return stk.top();
}


};
