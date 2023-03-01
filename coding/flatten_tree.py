class Node:
    """
    create node with lest and right attribute
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_pre_order(root):
    """
    this is pre order traversal
    """
    if root:
        # First print the data of root
        print(root.val),

        # Recursion function call left tree
        print_pre_order(root.left)

        # Recursion function call right tree
        print_pre_order(root.right)


def find(root, item):
    """
    search the given element in tree
    """
    if root:
        # check the element if it is in root
        if root.val == item:
            print("Tree " + str(root.val))
            if root.left is not None:
                print(" Left " + str(root.left.val))
            if root.right is not None:
                print(" Right " + str(root.right.val))
            return
        # Recursion function call left tree
        find(root.left, item)
        # Recursion function call right tree
        find(root.right, item)


tree_root = Node(1)
tree_root.left = Node(13)
tree_root.right = Node(10)
tree_root.left.left = Node(8)
tree_root.right.left = Node(1)
print("Pre order traversal:")
print_pre_order(tree_root)
find(tree_root, 1)