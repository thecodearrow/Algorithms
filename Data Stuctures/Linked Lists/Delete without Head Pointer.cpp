//https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/

#include<bits/stdc++.h>
using namespace std;

/*This is a function problem.You only need to complete the function given below*/

/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}*head;
*/
// This function should delete node from linked list. The function
// may assume that node exists in linked list and is not last node
// node: reference to the node which is to be deleted
void deleteNode(Node *node)
{  
   Node* temp=node->next;
   node->data=node->next->data;
   node->next=node->next->next;
   delete temp;

}
