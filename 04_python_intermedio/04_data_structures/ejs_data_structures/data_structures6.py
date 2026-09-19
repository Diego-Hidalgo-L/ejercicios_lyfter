
class Node:
    data: str
    prev: "Node"
    next: "Node"

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return self.data


class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def append(self, new_node):
        old_tail = self.tail

        if old_tail is None:
            self.tail = new_node
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            old_tail.next = new_node
            new_node.prev = old_tail
            new_node.next = None
            self.tail = new_node

    def prepend(self, new_node):
        old_head = self.head

        if old_head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            old_head.prev = new_node
            new_node.next = old_head
            new_node.prev = None
            self.head = new_node

    def delete(self, data):
        current_node = self.head

        if current_node is None:
            print("The Double-Ended List is empty.")
        else:
            while current_node.data is not data:
                current_node = current_node.next

            current_node.prev = current_node.next
            return current_node.data
        

    def print_forward(self):
        current_node = self.head
        node_data = []

        if current_node is None:
            print("The Double-Linked List is empty.")
        else:
            while current_node is not None:
                node_data.append(current_node.data)
                current_node = current_node.next
        
        print(" -> ".join(node_data))

    def print_backward(self):
        current_node = self.tail
        node_data = []

        if current_node is None:
            print("The Double-Linked List is empty.")
        else:
            while current_node is not None:
                node_data.append(current_node.data)
                current_node = current_node.prev

        print(" -> ".join(node_data))


first_node = Node("C")
second_node = Node("B")
third_node = Node("A")
fourth_node = Node("X")

dll = DoubleLinkedList()

dll.append(third_node)
dll.append(second_node)
dll.append(first_node)
dll.prepend(fourth_node)

dll.print_forward()
dll.print_backward()