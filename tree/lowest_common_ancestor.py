# Easiest version: when nodes have parent
class Node:
    def __init__(self):
        parent = Nonee
        val = None
        left = None
        right = None
        
def lowest_common_ancestor(a, b):
    nodes1_history = Set()
    node1 = a
    while node1 != None:
        node1_history.add(node1)
        node1 = node1.parent
    
    nodes2 = b
    while node2 != None:
        if node2 in nodes1_history:
            return node2
        node2 = node2.parent
        
    return None    
    
# When the tree is a binary search tree, and no parent    
class Node:
    def __init__(self): 
        val = None
        left = None
        right = None
    
    def lowest_common_ancestor(root.left, a, b):
        if root == None:
            return None
        if root.val > a.val && root.val > b.val:
            return lowest_common_ancestor(root.left, a, b)
        if root.val < a.val && root.val < b.val:
            return lowest_common_ancestor(root.right, a, b)
        return root

# When the tree is just a binary tree, and no parent
class Node:
    def __init__(self):
        val = None
        left = None
        right = None
    
    def lowest_common_ancestor(root, a, b):
        if root == None:
            return None
        if root == a || root == b:
            return root
        left = lowest_common_ancestor(root.left, a, b)
        right = lowest_common_ancestor(root.right, a, b)
        if left != None && right != None:
            return root
        else if left != None:
            return left
        else if right != None:
            return right
        else:
            return None
