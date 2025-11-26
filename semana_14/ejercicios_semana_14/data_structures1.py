
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

    def push(self, new_node):
        current_top = self.top
        self.top = new_node
        new_node.next = current_top

    def pop(self):
            if self.top == None:
                print("The stack is empty. There is nothing to 'pop'.")
            else:
                self.top = self.top.next

    def print_structure(self):
        current_node = self.top

        if current_node == None:
            print("The stack is empty.")
            return

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next



my_stack = Stack()

first_node = Node("1) This is the first node.")
my_stack.push(first_node)

second_node = Node("2) This is the second node.")
my_stack.push(second_node)

third_node = Node("3) This is the third node.")
my_stack.push(third_node)

my_stack.print_structure()

print("Popping last node.")
my_stack.pop()
my_stack.print_structure()