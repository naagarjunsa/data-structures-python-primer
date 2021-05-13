from SinglyLinkedList import SinglyLinkedList

def reverse(llist):

    prev = None
    curr = llist.head
    
    while curr:
        next = curr.next    
        curr.next = prev
        prev = curr
        curr = next
    
    llist.head = prev

if __name__ == "__main__":
        
    llist = SinglyLinkedList()

    for i in range(5):
        llist.append(i*10)

    llist.print_list()

    reverse(llist)

    llist.print_list()

