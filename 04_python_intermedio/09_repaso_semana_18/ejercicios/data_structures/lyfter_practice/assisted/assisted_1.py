
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self, head):
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
        if self.head is None:
            print("The Queue is empty")
        else:
            self.head = self.head.next

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)

queue = Queue(primer_nodo)

print("Agregando un elemento")
queue.enqueue(Node("Soy el nuevo nodo!"))

queue.print_structure()

print("Quitando un elemento")
queue.dequeue()

queue.print_structure()