class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,  data):
        if self.data:
            if (data < self.data):
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif (data > self.data):
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
  
def height(node):
    if node is None:
        return 0
    return max(node.left.height() + node.right.height()) + 1   
def diameter(node):
    
    if node is None:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)
    
    ldiameter = diameter(node.left)
    rdiameter = diameter(node.right)
    
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

