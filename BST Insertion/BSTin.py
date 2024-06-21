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

def main():
    root = None
    elements = list(map(int, input("Enter the elements to insert into the BST (separated by spaces): ").split()))
    for elem in elements:
        root = insert(root, elem)
    
    print("In-order traversal of the BST:")
    in_order(root)
    print("\n")

if __name__ == "__main__":
    main()
