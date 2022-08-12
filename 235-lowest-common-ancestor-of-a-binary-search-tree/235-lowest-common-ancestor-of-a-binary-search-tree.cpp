/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return dfs(root, p, q);
    }
    
    
    TreeNode* dfs(TreeNode* node, TreeNode* p, TreeNode* q){
        if (node == NULL || node == p || node == q) return node;
        
        
        if (p->val < node->val && q->val < node->val) return dfs(node->left, p, q);
        
        if (p->val > node->val && q->val > node->val) return dfs(node->right, p, q);
            
        return node;
        
        
    }
};