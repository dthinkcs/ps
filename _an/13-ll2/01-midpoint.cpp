node* midpoint_linkedlist(node *head){
    if(head == NULL || head->next == NULL) {
        return head;
    }
    node *slow = head, *fast = head->next;
    while(fast != NULL && fast-> next != NULL) {
        slow = slow -> next;
        fast = fast -> next -> next;
    }
    return slow;
}
