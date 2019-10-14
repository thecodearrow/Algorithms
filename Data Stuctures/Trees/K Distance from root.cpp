/*This is a function problem.You only need to complete the function given below*/
/* A binary tree node has data, pointer to left child
   and a pointer to right child /
struct Node
{
    int data;
    Node* left;
    Node* right;
}; */
// function should print the nodes at k distance from root


/*Recursive Solution*/

void printKdistance(Node *root, int k)
{
  // Your code here
    if(k==0){
        cout<<root->data<<" ";
    }
    else{
        if(root->left!=NULL){
        printKdistance(root->left,k-1);
        }
        if(root->right!=NULL){
            printKdistance(root->right,k-1);
        }
        
        
    }
}


