
class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Dll:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def append(self, data):
        new_node = Node(data)
        old_tail = self.tail

        if old_tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        old_head = self.head

        if old_head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head.prev = new_node
            new_node.next = old_head
            self.head = new_node

    def delete(self, data):
        current_node = self.head

        while current_node is not None and current_node.data != data:
            current_node = current_node.next
        
        if current_node is None:
            raise ValueError("Data not found")
        
        if current_node == self.head:
            self.head = current_node.next

        if current_node == self.tail:
            self.tail = current_node.prev

        if current_node.prev is not None:
            current_node.prev = current_node.next

        if current_node.next is not None:
            current_node.next.prev = current_node.prev

        current_node.next = None
        current_node.prev = None
        
        return current_node.data

    def print_forward(self):
        current_node = self.head
        node_data = ["HEAD"]

        if current_node is None:
            print("The List is empty")
            return
        
        while current_node is not None:
            node_data.append(current_node.data)
            current_node = current_node.next
        
        node_data.append("TAIL")
        print(" <-> ".join(str(node) for node in node_data))

    def print_backward(self):
        current_node = self.tail
        node_data = ["TAIL"]

        if current_node is None:
            print("The list is empty")
            return
        
        while current_node is not None:
            node_data.append(current_node.data)
            current_node = current_node.prev
        
        node_data.append("HEAD")
        print(" <-> ".join(str(node) for node in node_data))


dll = Dll()

dll.append("A")
dll.append("B")
dll.append("C")
dll.prepend("X")

dll.print_forward()
dll.print_backward()