class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def max_value(a, b):
    return a if a > b else b

def get_balance_factor(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max_value(get_height(y.left), get_height(y.right)) + 1
    x.height = max_value(get_height(x.left), get_height(x.right)) + 1

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max_value(get_height(x.left), get_height(x.right)) + 1
    y.height = max_value(get_height(y.left), get_height(y.right)) + 1

    return y

def insert(node, key):
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max_value(get_height(node.left), get_height(node.right))

    balance_factor = get_balance_factor(node)

    # Left Left Case
    if balance_factor > 1 and key < node.left.key:
        return right_rotate(node)

    # Right Right Case
    if balance_factor < -1 and key > node.right.key:
        return left_rotate(node)

    # Left Right Case
    if balance_factor > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance_factor < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def preorder_traversal(root):
    if root:
        print(root.key, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Function to take user input and insert into AVL tree
def take_user_input():
    root = None
    while True:
        user_input = input("Enter a number to insert into the AVL tree (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            key = int(user_input)
            root = insert(root, key)
            print("Inserted", key)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return root

if __name__ == "__main__":
    root = take_user_input()
    if root:
        print("\nPreorder traversal of the constructed AVL tree:")
        preorder_traversal(root)
