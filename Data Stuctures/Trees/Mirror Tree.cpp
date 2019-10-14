//https://practice.geeksforgeeks.org/problems/mirror-tree/1

/*This is a function problem.You only need to complete the function given below*/
//function Template for C++
/* A binary tree node has data, pointer to left child
   and a pointer to right child /
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
}; */
/* Should convert tree to its mirror */
void mirror(Node* node) 
{
     // Your Code Here
     if(node->left==NULL && node->right==NULL){
         return;
     }
    if(node->left!=NULL){
        mirror(node->left);
    }
    if(node->right!=NULL){
        mirror(node->right);
    }
    
    //Swap left and right nodes
    Node *temp=node->left;
    node->left=node->right;
    node->right=temp;
   
     
}