from SinglyLinkedList import SinglyLinkedList

def remove_duplicates(llist):

    curr = llist.head
    data = dict()
    prev = None

    while curr:
        if curr.val in data:
            prev.next = curr.next
            curr = None
        else:
            data[curr.val] = 1
            prev = curr
        curr = prev.next

    curr = llist.head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    
if __name__ == "__main__":

    llist = SinglyLinkedList()

    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(2)
    llist.append(1)

    llist.print_list()
    remove_duplicates(llist)



        

    