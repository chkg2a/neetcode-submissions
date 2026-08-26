class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
            int i = 0;
      int n = matrix.size();
      int m = matrix[0].size();
      int j = (n * m) - 1;
      int counter = 0;
      int x = 0;
      int seen = 0;
      while (i <= n){
        int mid = n - (n + i) / 2;
        if(matrix[mid][0] == target) return true;
        else if(matrix[mid][0] < target) {
          if(seen == mid) break;
          seen = mid;
          i = mid + 1;
        }else{
          n = mid - 1;
        }
      }
      i = 0;
      while (i <= m){
        int mid = m - (m + i) / 2;
        if(matrix[seen][mid] == target) return true;
        else if(matrix[seen][mid] < target) {
          i = mid + 1;
        }else{
          m = mid - 1;
        }
      }
      return false;
  
    }
};
