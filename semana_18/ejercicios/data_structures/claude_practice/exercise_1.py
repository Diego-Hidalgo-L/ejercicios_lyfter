
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head=None):
        self.head = head
    
    def __len__(self):
        current_node = self.head
        count = 0

        while current_node is not None:
            count += 1
            current_node = current_node.next
        
        return count

    def insert_front(self, data):
        new_node = Node(data)

        old_head = self.head
        self.head = new_node
        new_node.next = old_head

    def insert_back(self, data):
        new_node = Node(data)
        current_node = self.head

        if self.head is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert_at(self, index, data):
        if index < 0:
            raise IndexError("Negative index")
        
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            current_index = 0

            while current_node is not None and current_index < index -1:
                current_node = current_node.next
                current_index += 1
            
            if current_node is None:
                raise IndexError("Index out of range")
            else:
                new_node.next = current_node.next
                current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        previous_node = None

        if current_node is None:
            print("The LinkedList is empty")
        else:
            while current_node is not None:
                if current_node.data == data:
                    if previous_node is None:
                        self.head = current_node.next # Este desconecta
                    else:
                        previous_node.next = current_node.next # Este desconecta
                    
                    return current_node
                
                previous_node = current_node # Estos pasan de nodo a nodo
                current_node = current_node.next

    def delete_at(self, index):
        if index < 0:
            raise IndexError("Negative index")
        
        if self.head is None:
            raise IndexError("Empty list")
        
        if index == 0:
            removed = self.head
            self.head = self.head.next
            return removed
        else:
            current_node = self.head
            current_index = 0

            while current_node.next is not None and current_index < index - 1:
                current_node = current_node.next
                current_index += 1
            
            if current_node.next is None:
                raise ValueError("Index out of range")
            else:
                removed = current_node.next
                current_node.next = removed.next

                return removed

    def find(self, data):
        current_node = self.head
        index = 0

        while current_node is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1
        
        return -1

    def reverse(self):
        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next

            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node
        
        self.head = prev_node

    def print_all(self):
        current_node = self.head
        node_data = []

        if current_node is None:
            print("The LinkedList is empty")
        else:
            while current_node is not None:
                node_data.append(str(current_node.data))
                current_node = current_node.next

        node_data.append("None")
        
        print(" -> ".join(str(node) for node in node_data))