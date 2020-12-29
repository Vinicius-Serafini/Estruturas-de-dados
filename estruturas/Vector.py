class Vector:

    def __init__(self, size):
        
        self.__data = [None] * size
        self.__last = -1
    
    def __str__(self):

        data = str(self.__data)

        return data
    
    def add(self, value):
        
        self.__grow()
        self.__last += 1
        self.__data[self.__last] = value

    def insert(self, index, value):
        
        self.__grow()
        last = self.__last 

        # Todo numero a frente do index será passado uma casa a frente
        if last >= index:
            for i in range(last, index - 1, -1):
                self.__data[i + 1] = self.__data[i]
  
        self.__data[index] = value
        self.__last += 1

    def __grow(self):
        
        if len(self.__data) == self.__last + 1:
            size = int(len(self.__data) * 1.5)
            copy = [None] * size

            for index in range(len(self.__data)):
                copy[index] = self.__data[index]

            self.__data = copy
    
    def search(self, value):
        
        # Retorna -1 se não encontrar
        for index in range(len(self.__data)):
            if value == self.__data[index]:
                return index
        
        return -1
    
    def get(self, index):
    
        return self.__data[index]
    
    def remove(self, index):

        if 0 <= index <= self.__last :
            for i in range(index, self.__last):
                self.__data[i] = self.__data[i + 1]
            self.__last -= 1
    
    def delete(self, value):

        index = self.search(value)
        self.remove(index)
            