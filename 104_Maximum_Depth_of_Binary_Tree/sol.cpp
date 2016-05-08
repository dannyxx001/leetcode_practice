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
        int maxDepth(TreeNode* root) {
            if(root == NULL)
                return 0;
            int l_max = 1, r_max = 1;
            if(root->left != NULL)
                l_max += maxDepth(root->left);
            if(root->right != NULL)
                r_max += maxDepth(root->right);
            return max(l_max,r_max);
        }
};
