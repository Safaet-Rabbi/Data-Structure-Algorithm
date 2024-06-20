class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size  # Initialize array with None values

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        print(self.array)

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        # Shift elements to the right
        self.array.append(None)  # Increase the size of the array by one
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        # Insert the value
        self.array[index] = value
        self.size += 1

    def delete(self, index):
        if 0 <= index < self.size:
            # Shift elements to the left
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]

            # Set the last element to None and decrease size
            self.array[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError("Index out of bounds")

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    arr = Array(size)

    print("Setting values in the array:")
    for i in range(size):
        value = input(f"Enter the value for index {i}: ")
        arr[i] = value

    print("\nArray after setting values:")
    arr.display()

    # Inserting a value
    index_to_insert = int(input("\nEnter the index to insert a value: "))
    value_to_insert = input("Enter the value to insert: ")
    try:
        arr.insert(index_to_insert, value_to_insert)
        print("\nArray after insertion:")
        arr.display()
    except IndexError as e:
        print(e)

    # Deleting an element
    index_to_delete = int(input("\nEnter the index to delete an element: "))
    try:
        arr.delete(index_to_delete)
        print("\nArray after deletion:")
        arr.display()
    except IndexError as e:
        print(e)
