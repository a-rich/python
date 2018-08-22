class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

def replace_node_in_parent(node, new_value=None):
    if node.parent:
        if node == node.parent.left:
            node.parent.left = new_value
        else:
            node.parent.right = new_value
    if new_value:
        new_value.parent = node.parent

def delete(node, key):
    if key < node.data:
        delete(node.left, key)
        return
    if key > node.data:
        delete(node.right, key)
        return
    if node.left and node.right:
        successor = node.right.find_min()
        node.data = successor.data
        delete(successor, successor.data)
    elif node.left:
        replace_node_in_parent(node.left)
    elif node.right:
        replace_node_in_parent(node.right)
    else:
        replace_node_in_parent(None)

def search(key, node):
    if node is None or node.data == key:
        return node
    if key < node.data:
        return search_recursively(key, node.left)
    return search_recursively(key, node.right)

def find_min(node):
    current_node = node
    while current_node.left:
        current_node = current_node.left
    return current_node

def find_max(node):
    current_node = node
    while current_node.right:
        current_node = current_node.right
    return current_node

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print root.data
    in_order_print(root.right)

def pre_order_print(root):
    if not root:
        return
    print root.data
    pre_order_print(root.left)
    pre_order_print(root.right)
