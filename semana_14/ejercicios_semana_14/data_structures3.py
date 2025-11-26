
class Node:
    data: str
    parent: "Node"
    left_child: "Node"
    right_child: "Node"

    def __init__(self, data, parent=None, left_child=None, right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    root: Node

    def __init__(self, root=None):
        self.root = root

    def set_root(self, new_node):
        if self.root:
            print("This Binary Tree already has a root.")
        else:
            self.root = new_node
    
    def create_left_child(self, parent, new_node):
        if self.root is None:
            print("This Binary Tree does not have a root.")
            return
        if parent.left_child:
            print("This parent node already has a left child.")
            return
        else:
            parent.left_child = new_node
            new_node.parent = parent
    
    def create_right_child(self, parent, new_node):
        if self.root is None:
            print("This Binary Tree does not have a root.")
            return
        elif parent.right_child:
            print("This parent node already has a right child.")
            return
        else:
            parent.right_child = new_node
            new_node.parent = parent

    def print_structure(self, node=None, level=0):
        if node is None:
            node = self.root
            if node is None:
                print("The Binary Tree is empty.")
                return
        
        print(" " * level + f"{node.data}")

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

tree.print_structure()
