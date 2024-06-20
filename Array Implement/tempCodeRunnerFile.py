class Array:
    def __init__(self, size, initial_value=None):
        self._size = size
        self._array = [initial_value] * size

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of bounds")

    def __setitem__(self, index, value):
        if 0 <= index < self._size:
            self._array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        print(self._array)

# Example usage
if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    initial_value = input("Enter the initial value for the array: ")
    arr = Array(size, initial_value)

    print("\nSetting values in the array:")
    while True:
        index = int(input("Enter the index to set the value (or -1 to stop): "))
        if index == -1:
            break
        value = input("Enter the value to set: ")
        try:
            arr[index] = value
        except IndexError as e:
            print(e)

    print("\nFinal array:")
    arr.display()

    print("\nGetting a value from the array:")
    index = int(input("Enter the index to get the value: "))
    try:
        print("Value at index", index, ":", arr[index])
    except IndexError as e:
        print(e)
