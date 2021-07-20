#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node *left;
    struct Node *right;

    Node(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

void inorder(struct Node *root){
    if(root==NULL){
        return;
    }
    inorder(root->left);
    cout << root->data << endl;
    inorder(root->right);
}

int main(){
    struct Node *root = new Node(1);
    cout << root->data << endl;
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    inorder(root);
}