#include<bits/stdc++.h>
using namespace std;

class bst{
    int data;
    bst *left;
    bst *right;
    public:
        bst(){
            data = 0;
            left = NULL;
            right = NULL;
        }

        bst(int val){
            data = val;
            left = NULL;
            right = NULL;
        }

        bst* insert(bst* root, int x){
            if(root==NULL){
                return new bst(x);
            }

            if(x > root->data){
                root->right = insert(root->right,x);
            }
            else{
                root->left = insert(root->left,x);
            }

            return root;
        }

        void inorder_print(bst *r){
            if(r==NULL)
                return;
            
            inorder_print(r->left);
            cout << r->data << endl;
            inorder_print(r->right);
        }
        
};

int main(){
    bst b1(12);
    bst* root = &b1;
    b1.insert(root,13);
    b1.insert(root,13);
    b1.inorder_print(root);
}