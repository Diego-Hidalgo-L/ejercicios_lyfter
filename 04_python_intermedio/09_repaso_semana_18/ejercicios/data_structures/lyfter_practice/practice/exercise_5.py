
class Node:
    data: str
    next: "Node"

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def insert_front(self, data):
        new_node = Node(data)

        old_head = self.head
        self.head = new_node
        new_node.next = old_head
    
    def insert_back(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
        
            current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        prev_node = None
        
        while current_node is not None and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return None
            
        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next
        
        current_node.next = None
        return current_node
        

    def print_all(self):
        current_node = self.head
        node_data = ["HEAD"]

        while current_node is not None:
            node_data.append(current_node.data)
            current_node = current_node.next
        
        node_data.append("None")
        print(" -> ".join(str(node) for node in node_data))

ll = LinkedList()

print("\nFront-inserting 10:")
ll.insert_front(10)
ll.print_all()

print("\nFront-inserting 20:")
ll.insert_front(20)
ll.print_all()

print("\nBack-inserting '30':")
ll.insert_back(30)
ll.print_all()

print("\nDeleting 10:")
ll.delete(10)
ll.print_all()