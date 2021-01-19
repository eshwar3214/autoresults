#include<stdio.h>
#include<stdlib.h>
typedef struct node{
    int data;
    struct node *left;
    struct node *right;
} node;
node *head=NULL;
int main()
{
    node *n=malloc(sizeof(node));
    n->data=3;
    n->left=NULL;
    n->right=NULL;
    head=n;
    n=malloc(sizeof(node));
    n->data=2;
    n->left=NULL;
    n->right=NULL;
    head->left=n;
    n=malloc(sizeof(node));
    n->data=4;
    n->left=NULL;
    n->right=NULL;
    head->right=n;
    printf(" %d %d %d",head->left->data,head->data,head->right->data);
    free(n);

    

    return 0;

}