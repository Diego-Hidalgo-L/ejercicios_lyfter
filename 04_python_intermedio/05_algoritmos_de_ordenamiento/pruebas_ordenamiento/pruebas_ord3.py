
class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head=None):
        self.head = head
    
    