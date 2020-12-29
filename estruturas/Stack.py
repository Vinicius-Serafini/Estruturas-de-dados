class Stack:

    def __init__(self, size):

        self.__data = [None] * size 
        self.__size = size
        self.__tos = -1

    def __str__(self):

        data = self.__data 
        size = self.__size 
        tos = data[self.__tos] if self.__tos >= 0 else None

        return f'Data: {data}\nSize: {size}\nTop of Stack: {tos}'
    
    def push(self, value):

        self.__tos = self.__tos + 1
        self.__data[self.__tos] = value
    
    def pop(self):

        if self.__tos >= 0:
            copy = self.__data[self.__tos]
            self.__data[self.__tos] = None;
            self.__tos = self.__tos - 1
            return copy 
    
    def print_data(self):
        
        print(self.__data)
