class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1  
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]
    
    def queue_size(self):
        return self.size
    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:", end=" ")
            index = self.front
            for _ in range(self.size):
                print(self.queue[index], end=" ")
                index = (index + 1) % self.capacity
            print()

def main():
    capacity = int(input("Enter the capacity of the circular queue: "))
    q = CircularQueue(capacity)
    
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display queue")
        print("4. Peek front")
        print("5. Queue size")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = input("Enter the item to enqueue: ")
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            front_item = q.peek()
            if front_item is not None:
                print(f"Front item is: {front_item}")
        elif choice == 5:
            print(f"Queue size is: {q.queue_size()}")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
