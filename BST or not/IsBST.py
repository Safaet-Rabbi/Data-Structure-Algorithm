class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_node(data):
    return Node(data)

def insert_node(root, data):
    if root is None:
        return create_node(data)
    else:
        if data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
    return root

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=' ')
        in_order(root.right)

def is_bst(root, prev=[None]):
    if root:
        if not is_bst(root.left, prev):
            return False
        if prev[0] and root.data <= prev[0].data:
            return False
        prev[0] = root
        return is_bst(root.right, prev)
    return True

def main():
    root = None
    print("Enter the elements to insert into the BST (separated by spaces):")
    elements = list(map(int, input().split()))
    for elem in elements:
        root = insert_node(root, elem)

    print("In-order traversal of the BST:")
    in_order(root)
    print("\n")

    if is_bst(root):
        print("This is a BST")
    else:
        print("This is not a BST")

if __name__ == "__main__":
    main()
