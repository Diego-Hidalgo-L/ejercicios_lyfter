
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data

class Queue:
    head: Node

    def __init__(self, head=None):
        self.head = head
    
    def enqueue(self, new_node):
        current_node = self.head

        if current_node is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
        
            current_node.next = new_node

    def dequeue(self):
        old_head = self.head

        if old_head:
            self.head = old_head.next
            return old_head
        else:
            print("The Queue is empty.")

    def print_all(self):
        current_node = self.head
        node_data = []

        if current_node is None:
            print("The Queue is empty.")

        while current_node is not None:
            node_data.append(current_node.data)
            current_node = current_node.next
        
        if not node_data:
            print("The Queue is empty.")
        else:
            print(" -> ".join(node_data))


head_node = Node("A")
my_queue = Queue()

my_queue.enqueue(head_node)

second_node = Node("B")
my_queue.enqueue(second_node)

third_node = Node("C")
my_queue.enqueue(third_node)

print("\nFirst structure:")
my_queue.print_all()

my_queue.dequeue()

print("\nStructure after dequeue:")
my_queue.print_all()