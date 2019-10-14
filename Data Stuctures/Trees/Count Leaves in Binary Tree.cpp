//https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1

/*This is a function problem.You only need to complete the function given below*/
//User function Template for C++
/* A binary tree node has data, pointer to left child
   and a pointer to right child  
struct Node
{
    int data;
    Node* left;
    Node* right;
}; */
/* Should return count of leaves. For example, return
    value should be 2 for following tree.
         10
      /      \ 
   20       30 */
int countLeaves(Node* root)
{
  // Your code here
  if(root==NULL){
      return 0;
  }
  if(root->left==NULL and root->right==NULL){
      return 1;
  }
  Node *leftNode=root->left;
  Node *rightNode=root->right;
  return countLeaves(leftNode)+countLeaves(rightNode);
}
