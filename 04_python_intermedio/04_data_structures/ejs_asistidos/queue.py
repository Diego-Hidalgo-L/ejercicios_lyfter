
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

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def enqueue(self, new_node):
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head:
            self.head = self.head.next


third_node = Node("Soy el tercer node.")
second_node = Node("Soy el segundo node.", third_node)
first_node = Node("Este es el primer node.", second_node)

queue = Queue(first_node)

print("Agregando un elemento!")

fourth_node = Node("Soy el nuevo nodo!")
queue.enqueue(fourth_node)
queue.print_structure()

print("\n")
print("Quitando un elemento!")

queue.dequeue()
queue.print_structure()