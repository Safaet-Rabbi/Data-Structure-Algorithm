class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_position(self, position, data):
        if position < 0:
            raise ValueError("Position must be non-negative")
        new_node = Node(data)
        if self.head is None:
            if position == 0:
                self.head = new_node
                new_node.next = self.head
            else:
                raise ValueError("Position out of bounds")
        elif position == 0:
            self.insert_at_beginning(data)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
                if current == self.head:
                    raise ValueError("Position out of bounds")
            new_node.next = current.next
            current.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            if current.data == value:
                if prev is None:  # Deleting the head node
                    if current.next == self.head:  # Only one node in the list
                        self.head = None
                    else:
                        # Find the last node
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = current.next
                        self.head = current.next
                else:
                    prev.next = current.next
                return
            else:
                prev = current
                current = current.next
            if current == self.head:
                break

    def delete_by_position(self, position):
        if self.head is None:
            return
        if position < 0:
            raise ValueError("Position must be non-negative")
        current = self.head
        prev = None

        if position == 0:
            if current.next == self.head:  # Only one node in the list
                self.head = None
            else:
                # Find the last node
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = current.next
                self.head = current.next
            return

        for _ in range(position):
            prev = current
            current = current.next
            if current == self.head:
                raise ValueError("Position out of bounds")

        prev.next = current.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Function to handle user input
def main():
    cll = CircularLinkedList()
    
    while True:
        print("\nChoose an option:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Insert at a specific position")
        print("4. Delete by value")
        print("5. Delete by position")
        print("6. Display list")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            cll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            cll.insert_at_end(data)
        elif choice == 3:
            position = int(input("Enter the position to insert at: "))
            data = int(input(f"Enter data to insert at position {position}: "))
            try:
                cll.insert_at_position(position, data)
            except ValueError as e:
                print(e)
        elif choice == 4:
            value = int(input("Enter value to delete: "))
            cll.delete_by_value(value)
        elif choice == 5:
            position = int(input("Enter the position to delete: "))
            try:
                cll.delete_by_position(position)
            except ValueError as e:
                print(e)
        elif choice == 6:
            cll.display()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
