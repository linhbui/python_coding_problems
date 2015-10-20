class Node:
    def __init__(self):
        val = None
        left = None
        right = None

    def check_binary_search_tree(node):
        return check_binary_search_tree_helper(node, float("-inf"), float("inf"))

    def check_binary_search_tree_helper(node, min_val, max_val): 
        if node == None:
            return True
        if node.val < min_val || node.val > max_val:
            return False
        left = check_binary_search_tree_helper(node.left, min_val, node.val)
        right = check_binary_search_tree_helper(node.right, node.val, max_val)
        return left && right
