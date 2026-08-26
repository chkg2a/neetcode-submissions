class Solution {
public:
    vector<int> twoSum(vector<int>& num, int target) {
        int o = 0;
        int p = num.size();
        for(int i =0;i<num.size();i++){
            if(num[o] + num[p-1] == target){
                return {o+1,p};
            }
            else if(num[o] + num[p-1] > target){
                p--;
            }
            else if(num[0] + num[p-1] < target){
                o++;
            }
        }
        return {};
    }
};
