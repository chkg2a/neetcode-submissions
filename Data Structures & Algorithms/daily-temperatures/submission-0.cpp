class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
          vector<int> output;
  for (int i = 0; i < temperatures.size(); i++) {
    int count = 0;
    for (int j = i; j < temperatures.size(); j++) {
      if (temperatures[i] < temperatures[j]) {
        break;
      } else if (j == temperatures.size() - 1) {
        count = 0;
      } else {
        count++;
      }
    }
    output.push_back(count);
  }
  return output;

    }
};
