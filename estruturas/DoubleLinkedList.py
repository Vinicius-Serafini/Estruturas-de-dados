class Node:

    def __init__(self, value):
        
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):

        value = self.value
        next_node = self.next.value 
        prev_node = self.prev.value
    
        return f'Node value: {value}\nNext value: {next_node}\nPrevious value: {prev_node}'

class DoubleLinkedList:

    def __init__(self):

        self.head = None 
        self.end = None 
        self.size = 0 


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

        if self.head == None:

            self.head = n 
            self.end = n 

        else:
            n.prev = self.end 
            
            if self.end != None:

                self.end.next = n 
            
            self.end = n 
        
        self.size += 1

    def insertOn(self, value, index):

        n = Node(value)

        if self.head == None and index == self.size:

            this.insert(value)

        else:

            if index == 0 :
                
                n.next = self.head 
                self.head.prev = n 
                self.head = n
                
            else:

                count = 1 
                current = self.head.next

                while count < index :
                    current = current.next
                    count += 1
                
                n.next = current 
                n.prev = current.prev 
                current.prev.next = n 
                current.prev = n

            self.size += 1

    def remove(self, value):
        
        current = self.head

        while current != None :  

            if current.value == value :

                if current != self.head and current != self.end:

                    current.next.prev = current.prev 
                    current.prev.next = current.next
                
                if current == self.head:
                    
                    if current.next != None:

                        current.next.prev = None 
                    
                    self.head = current.next
                
                if current == self.end:
                    
                    if current.prev != None:

                        current.prev.next = None 
                    
                    self.end = current.prev

                self.size -= 1
                return True 
            
            current = current.next

        return False 

    def search(self, value):

        current = self.head

        while current != None and current.value != value :

            current = current.next

        return current

    def print(self):

        saida = list()
        current = self.head 

        while current != None :
            saida.append(current.value)
            current = current.next

        print(saida)

    def printBackwards(self):

        saida = list()
        current = self.end

        while current != None :
            saida.append(current.value)
            current = current.prev

        print(saida)
