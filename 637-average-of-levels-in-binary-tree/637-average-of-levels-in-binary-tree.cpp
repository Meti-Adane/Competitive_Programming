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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> answer;
        queue<TreeNode*> que;
        que.push(root);
        while (que.size() > 0){
            long double levelSum = 0;
            int levelSize = que.size();
            for (int i = 0; i < levelSize; i++){
                TreeNode* temp = que.front();
                que.pop();
                levelSum += temp->val;
                if (temp->left != NULL) que.push(temp->left);
                if(temp->right != NULL) que.push(temp->right);
            }
            answer.push_back((levelSum / levelSize));
        }
        return answer;
            
    }
};