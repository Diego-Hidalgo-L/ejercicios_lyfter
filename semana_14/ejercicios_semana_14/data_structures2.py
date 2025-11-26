
class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def push_left(self, new_node):
        old_head = self.head

        if old_head == None:
            print("The Double-Ended Queue was empty.")
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.next = old_head
            new_node.prev = None
            old_head.prev = new_node
            self.head = new_node

    def pop_left(self):
        old_head = self.head

        if old_head == None:
            print("The Double-Ended Queue is empty. There is nothing to 'pop'.")
            return None
        elif self.head == old_head == self.tail:
            self.head = None
            self.tail = None
            old_head.next = None
            old_head.prev = None
            return old_head.data
        else:
            new_head = old_head.next
            new_head.prev = None
            self.head = new_head
            old_head.next = None
            old_head.prev = None
            return old_head.data

    def push_right(self, new_node):
        old_tail = self.tail

        if old_tail == None:
            # print("The Double-Ended Queue was empty.")
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            old_tail.next = new_node
            new_node.prev = old_tail
            new_node.next = None
            self.tail = new_node

    def pop_right(self):
        old_tail = self.tail

        if old_tail == None:
            # print("The Double-Ended Queue is empty. There is nothing to 'pop'.")
            return None
        elif self.head == old_tail == self.tail:
            self.head = None
            self.tail = None
            old_tail.next = None
            old_tail.prev = None
            return old_tail.data
        else:
            new_tail = old_tail.prev
            new_tail.next = None
            self.tail = new_tail
            old_tail.next = None
            old_tail.prev = None
            return old_tail.data

    def print_structure(self):
        current_node = self.head

        if current_node == None:
            print("The Double-Ended Queue is empty.")
            return
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def reverse_print_structure(self):
        current_node = self.tail

        if current_node == None:
            print("The Double-Ended Queue is empty.")
            return
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.prev
        


deque = DoubleEndedQueue()

first_node = Node("1) This is the first node.")
deque.push_right(first_node)


second_node = Node("2) This is the second node.")
deque.push_right(second_node)

deque.print_structure()

print("\n")
print("Adding zero_node.")
zero_node = Node("0) This node will go before 1 and 2.")
deque.push_left(zero_node)

deque.print_structure()

print("\n")
print("This is the reverse structure.")
deque.reverse_print_structure()

print("\n")
print("Removing the second node node.")
print()