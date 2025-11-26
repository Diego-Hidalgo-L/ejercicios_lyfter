
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self, top):
        self.top = top

    def push(self, new_node):
        current_node = self.top
        self.top = new_node
        new_node.next = current_node

    def pop(self):
            if self.top:
                self.top = self.top.next

    def print_structure(self):
        current_node = self.top

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next



first_node = Node("1) First node.")

my_stack = Stack(first_node)
my_stack.print_structure()

second_node = Node("2) Second node.")
my_stack.push(second_node)
my_stack.print_structure()

third_node = Node("3) Third node.")
my_stack.push(third_node)
my_stack.print_structure()

# my_stack.pop()
# my_stack.print_structure()