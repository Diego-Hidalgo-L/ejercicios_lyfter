
class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def bubble_sort(self):
        current_node = self.head

        while current_node.next is not None:
            if current_node.data > current_node.next.data:
                print("Intercambiando nodos...")
                self.head = current_node.next
                current_node.next = current_node
            else:
                print(f"{current_node.data} no es mayor que {current_node.next.data}")
                current_node = current_node.next


nodes = [1, 3, 2]

second_node = Node(2)
third_node = Node(3, second_node)
first_node = Node(1, third_node)

my_ll = LinkedList(first_node)


print(len(my_ll))