// Code learnt and modified from https://www.codesdope.com/blog/article/linked-list-traversal-using-loop-and-recursion-in-/

#include<bits/stdc++.h>
using namespace std;

struct node{
    int data;
    node *next;
};

class linkedlist{
    private:
        node *head, *tail;
    public:
        linkedlist(){
            head = NULL;
            tail = NULL;
        }

        void push_node(int x){
            node *temp = new node;
            temp->data = x;
            temp->next = NULL;

            if(head == NULL){
                head = temp;
                tail = temp;
            }
            else{
                tail->next = temp;
                tail = temp;
            }
        }

        node *gethead(){
            return head;
        }

        void print_linkedlist(){
            node *iter = head;
            while(iter != NULL){
                cout << iter->data << endl;
                iter = iter->next;
            }
        }

        void print_linkedlist(node *head){
            if(head==NULL){
                return;
            }
            else{
                cout << head->data << endl;
                print_linkedlist(head->next);
            }
        }

        void concatenate(node *head1, node *head2){
            if(head1->next != NULL){
                concatenate(head1->next,head2);
            }
            else{
                head1->next = head2;
            }
        }

        int get_length(){
            node *iter = head;
            int ll_len = 0;
            while(iter != NULL){
                ll_len++;
                iter = iter->next;
            }
            return ll_len;
        }
};

int main(){
    linkedlist a,b;
    a.push_node(1);
    a.push_node(2);
    a.push_node(3);
    b.push_node(4);
    b.push_node(5);
    b.push_node(6);
    a.print_linkedlist(a.gethead());
    cout << a.get_length() << endl;
    a.concatenate(a.gethead(),b.gethead());

    a.print_linkedlist(a.gethead());
    cout << a.get_length() << endl;
    return 0; 
}