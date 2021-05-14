class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class SinglyLinkedList:

    '''
        Contains the definition of a Singly Linked List

        Properties:
            - head : the head node of the list
        
        Methods
            - prepend : adds new node to start of the list
            - append : adds new node to end of the list
            - insert_after_node : inserts a new node after a specific node
            - delete_by_val : deleted node based on node val
            - delete_by_pos : deleted node based on position
            - get_length : returns length of list iterative
            - get_length_recursive : returns length of list recursive
    '''

    def __init__(self):
        self.head = None
    
    
    def prepend(self, val):
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node
    
    
    def append(self, val):
        new_node = Node(val)

        #head is None
        if self.head is None:
            self.head = new_node
            return
        
        #head is not None
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insert_after_node(self, prev_node, val):

        if prev_node is None:
            print("Previous Node does not exist")
            return
        
        new_node = Node(val)

        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node
    
    
    def delete_by_val(self, val):

        #delete at head
        curr = self.head
        if curr and curr.val == val:
            self.head = curr.next
            curr = None
            return
        
        #delete other than head
        prev = None
        while curr and curr.val != val:
            prev = curr
            curr = curr.next
        
        if curr is None:
            print("element not found in the list")
            return
        
        prev.next = curr.next
        curr = None

    
    def delete_by_pos(self, pos):

        curr = self.head
        count = 0

        #delete at pos 0
        if curr and pos == count:
            self.head = curr.next
            curr = None
            return
        
        #delete at pos > 0
        prev = None
        while curr and count != pos:
            prev = curr
            curr = curr.next
            count += 1
        
        if curr is None:
            print("pos greater than length")
            return
        
        prev.next = curr.next
        curr = None

    def get_length(self):
        
        curr = self.head
        length = 0
        
        while curr :
            curr = curr.next
            length += 1
        return length
    
    def get_length_recursive(self, node):

        if node is None:
            return 0
        return 1 + self.get_length_recursive(node.next)
    
    def print_list(self):

        if self.head is None:
            print("Empty List")
        
        curr = self.head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")
    
 
if __name__ == "__main__":

    llist = SinglyLinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")

    llist.print_list() 

    llist.prepend("Z")
    llist.prepend("Y")

    llist.print_list() 

    llist.insert_after_node(llist.head.next.next, "D")

    llist.print_list() 

    llist.delete_by_val("Y")
    llist.delete_by_val("E")
    llist.delete_by_val("B")

    llist.print_list() 

    llist.delete_by_pos(0)
    llist.delete_by_pos(2)

    llist.print_list()


