from SinglyLinkedList import SinglyLinkedList

def swap_pairs(llist):

    curr = llist.head
    prev = None
    is_first = True

    while curr:
        if is_first:
            first = curr
            curr = curr.next
        else:
            second = curr
            #first link
            if prev is None:
                llist.head = second
            else:
                prev.next = second
            
            #second and third links
            nxt = curr.next
            curr.next = first
            first.next = nxt

            #for next iteration
            curr = nxt
            prev = first
        is_first = not is_first
    
    return llist


if __name__ == "__main__":

    llist = SinglyLinkedList()

    for i in range(8):
        llist.append(i)

    llist.print_list()
    swap_pairs(llist).print_list()
