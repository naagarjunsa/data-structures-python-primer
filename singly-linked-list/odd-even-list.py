from SinglyLinkedList import SinglyLinkedList

def odd_even_list(llist):
        
    if not llist.head or not llist.head.next:
        return llist.head
    
    curr = llist.head
    new_head = new_curr = None
    
    while curr and curr.next:
        
        if not new_head:
            new_head = curr.next
            new_curr = new_head
        else:
            new_curr.next = curr.next
            new_curr = new_curr.next
        
        curr.next = curr.next.next
        if curr.next:
            curr = curr.next
    
    
    new_curr.next = None
    curr.next = new_head
    
    return llist


if __name__ == "__main__":

    llist = SinglyLinkedList()

    for i in range(8):
        llist.append(i)

    llist.print_list()
    odd_even_list(llist).print_list()
