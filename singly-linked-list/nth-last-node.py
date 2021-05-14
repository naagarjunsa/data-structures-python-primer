from SinglyLinkedList import SinglyLinkedList

def nth_last_node(llist, n):

    if n <= 0:
        print("invalid input for n")
        return
    
    front = llist.head
    back = llist.head

    while front and n:
        front = front.next
        n -= 1
    
    if n:
        print("length is less than n")
        return
    
    while front:
        front = front.next
        back = back.next
    
    return back.val

if __name__ == "__main__":

    llist = SinglyLinkedList()

    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    print(nth_last_node(llist, 1))
    print(nth_last_node(llist, 3))
    print(nth_last_node(llist, 5))
