#define MAXSIZE 100
class MinStack {
  int atTop;
  int *data;
  stack<int> stk;

public:
  MinStack() {
    data = new int[MAXSIZE];
    atTop = -1;
  }

  void push(int val) {
    if (atTop == MAXSIZE - 1) {
      return;
    }
    data[++atTop] = val;
    if (atTop == 0) {
      stk.push(val);
      return;
    }
    if (stk.top() <= data[atTop]) {
      stk.push(stk.top());
    } else {
      stk.push(val);
    }
  }


  void pop() {
    if (atTop == -1) {
      return;
    }
    stk.pop();
    atTop--;
  }

  int top() { return data[atTop]; }

  int getMin() { return stk.top(); }
};
