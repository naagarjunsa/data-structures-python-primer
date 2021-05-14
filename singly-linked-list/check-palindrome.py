from SinglyLinkedList import SinglyLinkedList

def check_palindrome(llist):

    #reverse the first half of the list
    # compare it with second half   
    fast = llist.head
    slow = llist.head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    

    prev = None
    curr = llist.head
    
    while curr and curr != slow:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    # to adjust the even-odd length of list
    if fast and not fast.next:
        slow = slow.next
        
    while prev and slow:
        if prev.val != slow.val:
            return False
        prev = prev.next
        slow = slow.next
        
    return True

if __name__ == "__main__":

    llist = SinglyLinkedList()

    llist.append(1)
    llist.append(2)
    llist.append(2)
    llist.append(1)

    print(check_palindrome(llist))

