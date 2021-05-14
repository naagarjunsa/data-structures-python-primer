from SinglyLinkedList import SinglyLinkedList, Node

def remove_duplicates_sorted_ii(llist):

    sentinel = Node(0, llist.head)
    
    pred = sentinel
    
    head = llist.head
    while head:
        
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            
            pred.next = head.next
        else:
            pred = pred.next
        
        head = head.next
    
    llist.head = sentinel.next
    return

if __name__ == "__main__":
        
    llist = SinglyLinkedList()

    llist.append(1)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(3)

    llist.print_list()

    remove_duplicates_sorted_ii(llist)
    llist.print_list()
