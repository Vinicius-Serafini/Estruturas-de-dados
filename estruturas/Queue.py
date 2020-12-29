class Queue:

    def __init__(self, size):

        self.__data = [None] * size 
        self.__size = size 
        self.__in_pos = 0
        self.__out_pos = 0
        self.__count = 0
    
    def __str__(self):

        structure = self.__data 
        data = self.__get_data()

        return (f'Structure: {structure}\nData: {data}')

    def enqueue(self, value):

        if self.__count < self.__size :
            self.__count += 1
            self.__data[self.__in_pos] = value 
            self.__in_pos = (self.__in_pos + 1) % self.__size 
    
    def dequeue(self):

        if self.__count > 0 :
            self.__count -= 1
            copy = self.__data[self.__out_pos]
            self.__out_pos = (self.__out_pos + 1) % self.__size 

    def __get_data(self):
        
        saida = list()
        i = self.__out_pos
        
        while i != self.__in_pos:
            saida.append(self.__data[i])
            i = (i + 1) % self.__size 
        
        return saida

    def print_data(self):
        
        data = self.__get_data()

        print(data)
    