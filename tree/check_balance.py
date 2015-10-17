class Node:
    def __init__(self):
        val = None
        left = None
        right = None
    
    def check_balance(node):
        if node == None:
            return True
        check_balance_rec(node) != -1    
    
    def check_balance_rec(node):
        if node == None:
            return 0
        left = check_balance_rec(node.left)
        right = check_balance_rec(node.right)
        
        if left == -1 || right == -1:
            return -1
        else if Math.abs(left - right) > 1:
            return -1
        else:
            return (left, right).max + 1
