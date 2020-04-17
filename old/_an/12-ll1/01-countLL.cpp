int length(Node *head) {
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input is handled automatically.
     */
    int count = 0;
    for (; head; head = head->next)
        count++;
    return count;

}
