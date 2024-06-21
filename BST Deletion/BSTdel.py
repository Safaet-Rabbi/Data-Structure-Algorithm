class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_node(data):
    return Node(data)

def insert(root, key):
    if root is None:
        return create_node(key)
    else:
        if key < root.data:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=' ')
        in_order(root.right)

def in_order_predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root

def delete_node(root, value):
    if root is None:
        return None
    
    if value < root.data:
        root.left = delete_node(root.left, value)
    elif value > root.data:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        temp = in_order_predecessor(root)
        root.data = temp.data
        root.left = delete_node(root.left, temp.data)
    return root

def main():
    root = None
    elements = list(map(int, input("Enter the elements to insert into the BST (separated by spaces): ").split()))
    for elem in elements:
        root = insert(root, elem)

    print("In-order traversal of the BST:")
    in_order(root)
    print("\n")

    delete_value = int(input("Enter the value to delete from the BST: "))
    root = delete_node(root, delete_value)

    print("In-order traversal after deletion:")
    in_order(root)
    print("\n")

if __name__ == "__main__":
    main()
