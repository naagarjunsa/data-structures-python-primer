from SinglyLinkedList import SinglyLinkedList

def mergeInBetween(list1, a, b, list2):
        #               a    b
        #List 1 : 1 -> 2 -> 3 -> 4 -> None
        #           \         /
        #List 2 :      8 -> 9
        
        #finding node a
        node = list1.head
        for _ in range(1, a):
            node = node.next
        node_a = node
        
        #finding node b    
        for _ in range(b-a+2):
            node = node.next
        node_b = node
        
        #replace the node_a next with first 
        node_a.next = list2.head
        
        #find last
        node = list2.head
        while node.next:
            node = node.next
        
        #replace last next with node_b
        node.next = node_b
        
        return list1

if __name__ == "__main__":

    llist1 = SinglyLinkedList()

    llist1.append(1)
    llist1.append(2)
    llist1.append(3)
    llist1.append(4)
    llist1.append(5)

    llist2 = SinglyLinkedList()
    llist2.append(100001)
    llist2.append(100002)
    llist2.append(100003)

    mergeInBetween(llist1, 2, 3, llist2).print_list()
