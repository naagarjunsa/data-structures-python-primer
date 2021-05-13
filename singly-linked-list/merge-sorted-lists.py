from SinglyLinkedList import SinglyLinkedList

def merge_sorted_lists(list_1, list_2):

    first_list = list_1.head
    second_list = list_2.head

    small_node = None

    if not first_list:
        return second_list
    if not second_list:
        return first_list
    
    if first_list and second_list:
        if first_list.val <= second_list.val:
            small_node = first_list
            first_list = small_node.next
        else:
            small_node = second_list
            second_list = small_node.next
        new_head = small_node

    while first_list and second_list:
        if first_list.val <= second_list.val:
            small_node.next = first_list
            small_node = first_list
            first_list = small_node.next
        else:
            small_node.next = second_list
            small_node = second_list
            second_list = small_node.next
    
    if not first_list:
        small_node.next = second_list
    
    if not second_list:
        small_node.next = first_list
    
    return new_head

if __name__ == "__main__":

    list_1 = SinglyLinkedList()
    list_1.append(1)
    list_1.append(3)
    list_1.append(5)


    list_2 = SinglyLinkedList()
    list_2.append(2)
    list_2.append(4)
    list_2.append(6)


    print("List 1 : ")
    list_1.print_list()
    print("List 2 : ")
    list_2.print_list()
    print("Merged List : ")

    curr = merge_sorted_lists(list_1, list_2)

    while curr:
        print(curr.val, end="-> ")
        curr = curr.next
    print("None")




        
