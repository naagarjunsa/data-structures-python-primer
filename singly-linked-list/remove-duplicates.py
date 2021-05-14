from SinglyLinkedList import SinglyLinkedList

def remove_duplicates(llist):

    curr = llist.head
    data = dict()

    while curr:
        if curr.val not in data:
            data[curr.val] = 0
        else:
            data[curr.val] += 1
        curr = curr.next

    curr = llist.head
    prev = None

    while curr:
        if data[curr.val] > 0:
            if prev:
                prev.next = curr.next
            else:
                llist.head = curr.next
            data[curr.val] -= 1
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    
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



        

    