/*The Node structure is defined as
struct Node
{
    int key;
    Node *left, *right;
}; */
/*Complete the function below*/
#include <bits/stdc++.h>
using namespace std;

void kUtil(Node* root, int k, int& c)
{
    if (!root || c >= k)
        return;
    kUtil(root->right, k, c);
    c += 1;
    if (c == k)
    {
        cout << root->key << endl;
        return;
    }
    kUtil(root->left, k, c);
}


void kthLargest(Node* root, int k)
{
    int c = 0;
    kUtil(root, k, c);
}

// void inorder(Node* root, vector<int>& v)
// {
//     if (root){
//     inorder(root->left, v);
//     v.push_back(root->key);
//     inorder(root->right, v);

//     }
// }

// void kthLargest(Node *root, int k)
// {
//     //Your code here
//     vector<int> v;
//     inorder(root, v);
//     cout << v[v.size() - k] << endl;
// }
