class Node:
    def __init__(self):
        val = None
        left = None
        right = None

    def check_binary_search_tree(node):
        if node == None:
            return True
        if node.left != None && node.left > node.val 
            return False
        if node.right != None && node.right < node.val 
            return False
        left = check_binary_search_tree(node.left)
        right = check_binary_search_tree(node.right)
        return left && right
