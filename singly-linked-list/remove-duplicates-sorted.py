from SinglyLinkedList import SinglyLinkedList

def remove_duplicates_sorted(llist):

    if not llist.head:
        return llist.head
    
    curr, prev = llist.head.next, llist.head

    while curr:
        if curr.val == prev.val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return llist.head

if __name__ == "__main__":
        
    llist = SinglyLinkedList()

    llist.append(1)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(3)

    llist.print_list()

    remove_duplicates_sorted(llist)
    llist.print_list()
