class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> uset; 
        vector<int> arr;
        for(int i = 0; i < nums1.size();i++){
            uset.insert(nums1[i]);
        }
        for(int i = 0; i < nums2.size();i++){
            if(uset.count(nums2[i])) arr.push_back(nums2[i]);
        }
        return arr;
    }
};