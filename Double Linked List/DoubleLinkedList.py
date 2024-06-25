class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListTraversal(head):
    if head is None:
        return
    ptr = head
    while True:
        print(f"Element is {ptr.data}")
        ptr = ptr.next
        if ptr == head:
            break

def insertAtFirst(head, data):
    ptr = Node(data)
    if head is None:
        ptr.next = ptr  # Point to itself for circular list
        return ptr
    p = head
    while p.next != head:
        p = p.next
    # p now points to the last node in the circular list

    p.next = ptr
    ptr.next = head
    head = ptr
    return head

if __name__ == "__main__":
    # Initialize nodes
    head = Node(4)
    second = Node(3)
    third = Node(6)
    fourth = Node(1)

    # Link nodes
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = head

    print("Circular Linked list before insertion")
    linkedListTraversal(head)

    # Perform insertions at the beginning
    head = insertAtFirst(head, 54)
    head = insertAtFirst(head, 58)
    head = insertAtFirst(head, 59)

    print("Circular Linked list after insertion")
    linkedListTraversal(head)
