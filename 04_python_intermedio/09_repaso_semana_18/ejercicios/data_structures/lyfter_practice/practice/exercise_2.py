
class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Deque:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def push_left(self, data):
        new_node = Node(data)
        old_head = self.head

        if old_head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            new_node.next = old_head
            old_head.prev = new_node
            new_node.prev = None
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        old_tail = self.tail

        if old_tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            old_tail.next = new_node
            new_node.prev = old_tail
            new_node.next = None
            self.tail = new_node

    def pop_left(self):
        old_head = self.head

        if old_head is None:
            raise IndexError("The Double-Ended Queue is empty")
        elif old_head == self.tail:
            old_head.next = None
            old_head.prev = None
            self.head = None
            self.tail = None
            return old_head.data
        else:
            new_head = old_head.next
            new_head.prev = None
            self.head = new_head
            old_head.prev = None # Desconectar pointers
            old_head.next = None # Desconectar pointers
            return old_head.data

    def pop_right(self):
        old_tail = self.tail

        if old_tail is None:
            raise IndexError("The Double-Ended Queue is empty")
        elif old_tail == self.head:
            self.tail = None
            self.head = None
            old_tail.prev = None
            old_tail.next = None
            return old_tail.data
        else:
            new_tail = old_tail.prev
            new_tail.next = None
            self.tail = new_tail
            old_tail.prev = None
            old_tail.next = None
            return old_tail.data

    def print_structure(self):
        current_node = self.head
        node_data = ["HEAD"]

        if current_node is None:
            print("The Double-Ended Queue is empty")
            return None
        
        while current_node is not None:
            node_data.append(current_node.data)
            current_node = current_node.next
        
        node_data.append("TAIL")

        print(" <-> ".join(str(node) for node in node_data))
    
    def print_reverse(self):
        current_node = self.tail
        node_data = ["TAIL"]

        if current_node is None:
            print("The Double-Ended Queue is empty")
            return None
        
        while current_node is not None:
            node_data.append(current_node.data)
            current_node = current_node.prev

        node_data.append("HEAD")

        print(" <-> ".join(str(node) for node in node_data))


dq = Deque()

dq.push_right("1) This is the first node")

dq.push_right("2) This is the second node")

dq.print_structure()

print()
print("Adding zero_node:")
dq.push_left("0) This node will go before 1 and 2")

dq.print_structure()

print()
print("This is the reverse structure:")
dq.print_reverse()

print()
print("Removing the second node node:")
dq.pop_right()
dq.print_structure()
print()