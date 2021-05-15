from SinglyLinkedList import SinglyLinkedList

def swap_nodes(llist, val_1, val_2):

        if val_1 == val_2:
            return None
        
        #find the node and prev node of val_1
        prev_1 = None
        curr_1 = llist.head
        while curr_1 and curr_1.val != val_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        #find the node and prev node of val_2
        prev_2 = None
        curr_2 = llist.head
        while curr_2 and curr_2.val != val_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            print("node with the vals does not exist in the list")
            return
        
        #swap both the nodes, handle two cases if one of it head and one is not
        if prev_1:
            prev_1.next = curr_2
        else:
            llist.head = curr_2
        
if __name__ == "__main__":

    llist = SinglyLinkedList()

    for i in range(8):
        llist.append(i)

    llist.print_list()

    swap_nodes(llist, 3, 7)
    llist.print_list()
