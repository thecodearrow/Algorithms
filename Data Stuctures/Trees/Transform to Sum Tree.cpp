// https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1 

/*This is a function problem.You only need to complete the function given below*/
/* A binary tree node
struct Node
{
    int data;
    Node* left, * right;
}; */
// Convert a given tree to a tree where every node contains sum of values of
// nodes in left and right subtrees in the original tree
int constructSumTree(Node *node){
    if(node==NULL){
        return 0;
    }
    int leftSum=constructSumTree(node->left);
    int rightSum=constructSumTree(node->right);
    int currentSum=node->data;
    node->data=leftSum+rightSum;
    return currentSum+leftSum+rightSum;
}
void toSumTree(Node *node)
{
    // Your code here
    
    constructSumTree(node);
    
}

