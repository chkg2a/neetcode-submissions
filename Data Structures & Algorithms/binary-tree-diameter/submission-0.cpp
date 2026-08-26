/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int result = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        recursive(root);
        return result;
    }
    int recursive(TreeNode*root){
        if(!root) return 0;
        int left = recursive(root->left);
        int right = recursive(root->right);
        result = max(result,  left + right);
        return 1 + max(left, right);
    }
};
