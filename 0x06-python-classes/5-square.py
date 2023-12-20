#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """define a square."""
    def __init__(self, size=0):
        """initializing."""
        self.size = size

    @property
    def size(self):
        """getting or setting size"""
        return self.__size

    @size.setter
    def size(self, value):
        """define size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """return area square"""
        return self.__size ** 2

    def my_print(self):
        """print # for range of size"""
        if self.__size > 0:
            for _ in range(self.__size):
                print('#' * self.__size)
        else:
            print()
