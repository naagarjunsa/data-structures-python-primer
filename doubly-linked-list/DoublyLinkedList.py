class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            
            curr.next = new_node
            new_node.prev = curr

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_node_before(self, node, val):

        new_node = Node(val)
        new_node.next = node
        prev = node.prev
        node.prev = new_node

        if prev:
            prev.next = new_node
            new_node.prev = prev
        else:
            self.head = new_node
        
    
    def add_node_after(self, node, val):
        
        new_node = Node(val)

        new_node.prev = node
        nxt = node.next
        node.next = new_node
        
        if nxt:
            nxt.prev = new_node
            new_node.next = nxt
        

    def print_list(self):
        curr = self.head
        prev = None
        while curr:
            prev = curr
            print(curr.val, end="-> ")
            curr = curr.next
        print("None")

        while prev:
            print(prev.val, end= "-> ")
            prev = prev.prev
        print("None")
    
    def delete_node(self, val):

        if self.head is None:
            print("Empty list")
        
        if self.head.val == val:
            curr = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            curr = None
            return
        
        curr = self.head.next
        while curr:
            nxt = curr.next
            if curr.val == val:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            curr = None
            curr = nxt
        
    def reverse(self):

        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev


if __name__ == "__main__":

    llist = DoublyLinkedList()

    llist.append(1)
    llist.add_node_after(llist.head, 0)
    llist.append(2)
    llist.prepend(3)
    llist.prepend(5)
    llist.append(4)

    llist.add_node_before(llist.head, 9)
    llist.add_node_before(llist.head.next , 10)

    llist.add_node_after(llist.head , 11)
    llist.delete_node(9)
    llist.delete_node(4)
    llist.delete_node(3)
    llist.print_list()
    llist.reverse()
    llist.print_list()
