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
                node *iter=head;
                while(iter->next!=NULL){
                    iter = iter->next;
                }
                iter->next = temp;
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

        void insert_node(int pos, int value){
            if(this->head == NULL){
                this->push_node(value);
            }
            else{
                if(pos==0){
                    node *temp = new node;
                    temp->data = value;
                    temp->next = this->head;
                    this->head = temp;
                }
                else if(pos > this->get_length() - 1){
                    this->push_node(value);
                }
                else{
                    node *temp = new node;
                    temp->data = value;
                    node *prev_node = this->head;
                    
                    for(int i=0; i<pos-1; i++){
                        prev_node = prev_node->next;
                    }

                    temp->next = prev_node->next;
                    prev_node->next = temp;
                }

            }
        }

        void delete_node(int pos){
            if(pos>this->get_length()-1){
                cout << "Position Beyond LinkedList Length" << endl;
                return;
            }

            if(pos == 0){
                node *iter_node = this->head;
                this->head = this->head->next;
                delete iter_node;
                return;
            }

            node *iter_node = this->head;
            node *prev_node = this->head;
            for(int i=0; i<pos; i++){
                prev_node = iter_node;
                iter_node = iter_node->next;
            }
            prev_node->next = iter_node->next;
            delete iter_node;
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
    cout << " " << endl;

    a.concatenate(a.gethead(),b.gethead());

    a.print_linkedlist(a.gethead());
    cout << a.get_length() << endl;
    cout << " " << endl;

    a.insert_node(5,10);
    a.print_linkedlist(a.gethead());
    cout << a.get_length() << endl;
    cout << " " << endl;

    a.delete_node(6);
    a.print_linkedlist(a.gethead());
    cout << a.get_length() << endl;
    cout << " " << endl;

    return 0; 
}