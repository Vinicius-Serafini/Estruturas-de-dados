from functools import reduce

class Node:

    def __init__(self, value):
        
        self.value = value
        self.next = None
    
    def __str__(self):

        value = self.value
        next_node = self.next.value if self.next else None
    
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


class HashTable:

    def __init__(self):

        self.lists = [None] * 31

        for index in range(len(self.lists)):
            self.lists[index] = LinkedList()

    def __str__(self):

        lists = str([str(self.lists[x]) for x in range(len(self.lists))])

        return lists
    

    def __hashCode(self, value):

        hash_sum = reduce(lambda x, y: x + y, [ord(char) for char in value])
        hash_sum = hash_sum % len(value)

        return hash_sum % len(self.lists)

    
    def insert(self, value):

        assert isinstance(value, str), "Deve ser informado um dado do tipo String"

        pos = self.__hashCode(value)
        linked_list = self.lists[pos]
        linked_list.insert(value)

    def search(self, value):

        pos = self.__hashCode(value)
        linked_list = self.lists[pos]
        node = linked_list.search(value)

        return node 
    
    def remove(self, value):

        pos = self.__hashCode(value)
        linked_list = self.lists[pos]
        return linked_list.remove(value)

