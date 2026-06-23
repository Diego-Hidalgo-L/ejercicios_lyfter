
class Node:
    data: str
    next: "Node"

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self, head=None):
        self.head = head
    
    def enqueue(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            
            current_node.next = new_node

    def dequeue(self):
        old_head = self.head

        if old_head is None:
            raise IndexError("The Queue is empty")
        else:
            self.head = old_head.next
            return old_head.data

    def print_all(self):
        current_node = self.head
        node_data = ["HEAD"]

        if current_node is None:
            print("The Queue is empty")
            return
        else:
            while current_node is not None:
                node_data.append(current_node.data)
                current_node = current_node.next
            
            node_data.append("None")

        print(" -> ".join(str(node) for node in node_data))



queue = Queue()

queue.enqueue("Este es el primer node.")
queue.enqueue("Soy el segundo node.")
queue.enqueue("Soy el tercer node.")

print("Agregando un elemento!")

queue.enqueue("Soy el nuevo nodo!")
queue.print_all()

print("\n")
print("Quitando un elemento!")

queue.dequeue()
queue.print_all()