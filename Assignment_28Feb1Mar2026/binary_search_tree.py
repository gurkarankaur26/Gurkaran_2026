class Node():
    def __init__(self, num, left=None, right=None):
        self.Key = num
        self.Left = left
        self.Right = right

def insert(new_val, root_node):
    if root_node is None:
        return Node(new_val)

    # Use a temporary pointer to traverse
    current = root_node
    
    while True:
        if new_val < current.Key:
            if current.Left is None:
                current.Left = Node(new_val)
                break
            else:
                current = current.Left
        else: 
            if current.Right is None:
                current.Right = Node(new_val)
                break
            else:
                current = current.Right
    return root_node

def searchbst(val,root_node:Node):
    current = root_node
    while current is not None:            
            if val == current.Key:
               return True
            elif val < current.Key:
                current = current.Left
            else: 
                current = current.Right    
    return False       

def printbst(root_node:Node):
    if root_node is not None:        
            printbst(root_node.Left)
            print(root_node.Key)
            printbst(root_node.Right)
        


'''root = Node(23)
insert(10, root)
insert(11, root)
print(root.Key,root.Left.Key, root.Left.Right.Key)
insert(25, root)
# Result: 23(L:10(R:11), R:25)
print(root.Key,root.Right.Key,root.Left.Key)
insert(45, root)
searchbst(45,root)
printbst(root)'''