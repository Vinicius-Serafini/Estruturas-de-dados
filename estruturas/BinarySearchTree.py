class Node:

    def __init__(self, value):
        
        self.parent = None 
        self.left = None 
        self.right = None 
        self.key = value 
    
    def __str__(self):

        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        parent = self.parent.key if self.parent else None
        key = self.key

        return f'{{ Parent: {parent} | Right: {right} | Left: {left} | Key: {key} }}'
    
class BinarySearchTree:

    def __init__(self):
        
        self.root = None 

    def __str__(self):
        
        root = self.root;
        minimum = self.minimum(root)
        maximum = self.maximum(root)

        return f'Root: {root}\nMinimum: {minimum}\nMaximum: {maximum}'
        
    
    def insert(self, value):

        n = Node(value)

        if self.root == None:
            self.root = n 
        else:

            x = self.root 
            parent = self.root 

            while x != None:

                parent = x 

                if value < parent.key:
                    x = parent.left        
                else:
                    x = parent.right

            if value < parent.key:
                parent.left = n 
            else:
                parent.right = n 
            
            n.parent = parent
                
    def search(self, key):

        node = self.root 

        while node != None:
            if node.key == key:               
                return node            
            if key < node.key:
                node = node.left          
            else:
                c = c.right 
        
        return None 
    
    def maximum(self, node):
        
        n = node 

        while n.right != None:     
            n = n.right
        
        return n

    def minimum(self, node):

        n = node 

        while n.left != None:     
            n = n.left
        
        return n 
    
    def successor(self, node):
        
        if node.right != None:
            return self.minimun(node.right)        
        else:
            s = node.parent 

            while s.key < node.key:
                s = s.parent 
            
            return s 
    
    def __transplant(self, u, v):

        if u == self.root:
            self.root = v 
        elif u.parent.left == u:
            u.parent.left = v 
        else:
            u.parent.right = v 

        if v != None:
            v.parent = u.parent 
     
    def remove(self, node):

        if node.left == None:
            self.__transplant(node, node.right)
        elif node.right == None :
            self.__transplant(node, node.left)
        else:
            s = self.sucessor(node)
            if s.parent != node:
                self.__transplant(s, s.right)
                s.right = node.right
                s.right.parent = s 
            
            self.__transplant(node, s)
            s.left = node.left
            s.left.parent = s 
    