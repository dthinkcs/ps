BinaryTreeNode<int>* searchInBST(BinaryTreeNode<int> *root , int k){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */

    if (root == NULL)
        return NULL;

    if (root->data == k)
        return root;

    if (root->data < k)
        return searchInBST(root->right, k);

    else
        return searchInBST(root->left, k);

}
