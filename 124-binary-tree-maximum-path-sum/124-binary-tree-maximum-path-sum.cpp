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
    int ans = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        recurse(root);
        return ans;
    }
    
    
    int recurse(TreeNode* node){
        if (node == NULL) {
            return 0;
        }
        
        int leftSum = max(recurse(node->left), 0);
        int rightSum = max(recurse(node->right), 0);
        
        int path = leftSum + rightSum + node->val;
        ans = max(ans, path);
        
        return max(leftSum, rightSum) + node->val;
    }
};