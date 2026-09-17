
class Node:
    data: str
    next: "Node"

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        old_top = self.top

        if self.top is None:
            raise IndexError("The Stack is empty")
        else:
            self.top = old_top.next
            return old_top.data

    def print_structure(self):
        current_node = self.top

        if current_node is None:
            print("The Stack is empty")
            return
        else:
            print("TOP")
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
            print("BOTTOM")