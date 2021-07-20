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

class bst{
    struct Node* root;

    Node* insert_node(Node *recur, int x){
        if(recur==NULL){
            return new Node(x);
        }
        if(x > recur->data){
            recur->right = insert_node(recur->right,x);
        }
        else{
            recur->left = insert_node(recur->left,x);
        }
        return recur;
    }

    void inorder_print(Node* root){
        if(root==NULL)
            return;
        inorder_print(root->left);
        cout << root->data << " ";
        inorder_print(root->right);
    }

    public:
        bst(){
            root = NULL;
        }

        void insert(int x){
            root = insert_node(root, x);
        }

        void inorder_display(){
            inorder_print(root);
            cout << endl;
        }
};

int main(){
    bst b1;
    b1.insert(12);
    b1.insert(10);
    b1.insert(14);
    b1.insert(9);
    b1.inorder_display();
}