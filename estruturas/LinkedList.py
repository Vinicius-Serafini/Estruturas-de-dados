class Node:

    def __init__(self, value):
        
        self.value = value
        self.next = None
    
    def __str__(self):

        value = self.value
        next_node = self.next.value 
    
        return f'Node value: {value}\nNext value: {next_node}'


class LinkedList:

    def __init__(self):
    
        self.head = None 

    def __str__(self):

        saida = list()
        current = self.head 

        while current != None :
            saida.append(current.value)
            current = current.next

        saida = str(saida)

        return saida

    
    def insert(self, value):
    
        n = Node(value)
        n.next = self.head
        self.head = n 

    def remove(self, value):
        
        prev = None 
        current = self.head

        while (current != None):
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                
                return True 
            
            prev = current 
            current = current.next
        
        return False

    def search(self, value):
        
        current = self.head

        while (current != None and current.value != value):
            current = current.next 
        
        return current 
