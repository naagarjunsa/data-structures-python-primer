from SinglyLinkedList import SinglyLinkedList

def rotate_list(llist, k):
    
    head = llist.head
    if head is None:
        return head
    size = 0
    curr = head
    last = None
    while curr:
        last = curr
        curr = curr.next
        size += 1
    
    k = k % size
    
    if k == 0:
        return head
    
    #find the kth node
    fast = head
    new_head = head
    new_last = None
    
    for _ in range(k):
        fast = fast.next
    
    while fast:
        new_last = new_head
        new_head = new_head.next
        fast = fast.next
    
    new_last.next = None
    last.next = head
    head = new_head
    
    llist.head = head
    return llist

if __name__ == "__main__":

    llist = SinglyLinkedList()

    for i in range(8):
        llist.append(i)

    llist.print_list()
    rotate_list(llist, 2).print_list()
