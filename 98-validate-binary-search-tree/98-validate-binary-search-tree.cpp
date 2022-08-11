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
    long long MININT = LONG_MIN;
    long long MAXINT = LONG_MAX;
    
public:
    bool isValidBST(TreeNode* root) {
     return dfs(root, MAXINT, MININT);   
    }
    
    bool dfs(TreeNode* node, long long low, long long high){
        if (node == NULL) return true;
        
        if (node->val >= low || node->val <= high) return false;
        
        return (dfs(node->left, node->val, high) && dfs(node->right, low, node->val));
    
    }
};