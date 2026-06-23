
class Node:
    data: str
    parent: "Node"
    right_child: "Node"
    left_child: "Node"

    def __init__(self, data=None, parent=None, right_child=None, left_child=None):
        self.data = data
        self.parent = parent
        self.right_child = right_child
        self.left_child = left_child


class BinaryTree:
    root: Node

    def __init__(self, root=None):
        self.root = root

    def set_root(self, new_node):
        if self.root is not None:
            self.root = new_node
            return
        else:
            print("The Binary Tree already has a root")

    def create_left_child(self, parent, new_node):
        if self.root is None:
            print("The Binary Tree does not have a root")
            return
        elif parent.left_child:
                print("The parent node already has a left_child")
        else:
            parent.left_child = new_node
            new_node.parent = parent
    
    def create_right_child(self, parent, new_node):
        if self.root is None:
            print("The Binary Tree does not have a root")
            return
        elif parent.right_child:
            print("The parent node already has a right_child")
            return
        else:
            parent.right_child = new_node
            new_node.parent = parent
    
    def print_structure(self, node=None, level=0):
        if node is None:
            node = self.root
            if node is None: # Lo mismo que decir if self.root is None
                print("The Binary Tree is empty")
                return

        print("   " * level + f"{node.data}")

        if node.left_child:
            self.print_structure(node.left_child, level + 1)
        if node.right_child:
            self.print_structure(node.right_child, level + 1)


root = Node("A")
tree = BinaryTree(root)

b = Node("B")
c = Node("C")
d = Node("D")

tree.create_left_child(root, b)
tree.create_right_child(root, c)
tree.create_left_child(b, d)
tree.create_right_child(b, Node("E"))

tree.print_structure()
