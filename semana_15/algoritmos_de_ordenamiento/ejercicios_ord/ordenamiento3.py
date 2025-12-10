
class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def bubble_sort(self):
        swapped = True
        iterations = 0
        swaps = 0

        while swapped:
            current_node = self.head
            swapped = False
            while current_node.next is not None:
                if current_node.data > current_node.next.data:
                    temp_data = current_node.data
                    current_node.data = current_node.next.data
                    current_node.next.data = temp_data
                    swapped = True
                    swaps += 1

                current_node = current_node.next
            
            iterations += 1
        
        return iterations, swaps


# Así se vería el LinkedList antes del bubble sort:
# nodes = [3, 1, 4, 2]

second_node = Node(2)
fourth_node = Node(4, second_node)
first_node = Node(1, fourth_node)
third_node = Node(3, first_node)

def main():
    my_ll = LinkedList(third_node)

    print("\nStructure BEFORE the bubble sort:")
    my_ll.print_structure()

    iterations, swaps = my_ll.bubble_sort()

    print("\nStructure AFTER the bubble sort:")
    my_ll.print_structure()
    print("\nIterations:", iterations)
    print("Swaps:", swaps)


main()