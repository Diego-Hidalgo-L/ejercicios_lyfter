
class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    # def __str__(self):
    #     return self.data


class LinkedList:
    head: Node

    def __init__(self, head=None):
        self.head = head
    
    def insert_front(self, new_node):
        old_head = self.head
        self.head = new_node
        new_node.next = old_head

    def insert_back(self, new_node):
        current_node = self.head

        if current_node is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        previous_node = None

        if current_node is None:
            print("The LinkedList is empty.")
        else:
            while current_node.data is not data:   # si esto no sirve, intentar con current_node.data
                previous_node = current_node
                current_node = current_node.next
            if previous_node is None:
                self.head = current_node.next
            else:
                previous_node.next = current_node.next
            
            current_node.next = None
            return current_node

    def print_all(self):
        current_node = self.head
        node_data = []

        if current_node is None:
            print("The LinkedList is empty.")
        else:
            while current_node is not None:
                node_data.append(current_node.data)
                current_node = current_node.next
        
        print(" -> ".join(str(num) for num in node_data))


first_node = Node(10)
second_node = Node(20)

ll = LinkedList()

ll.insert_front(first_node)
ll.insert_front(second_node)

ll.print_all()

print("\nBack-inserting '30'.")
third_node = Node(30)
ll.insert_back(third_node)

ll.print_all()

ll.delete(10)

ll.print_all()