#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes using Rectangle class
        """
        super().__init__(size, size, x, y, id)
        self.id = self.id
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        returns string representation
        """
        result1 = "[Square] (" + str(self.id) + ") "
        result2 = str(self.__x) + "/" + str(self.__y) + " - "
        result3 = str(self.__width)
        return result1 + result2 + result3

    @property
    def size(self):
        """
        returns value of size
        """
        return self.__width

    @size.setter
    def size(self, size):
        """
        sets value of size
        """
        if type(size) == int:
            if size >= 0:
                self.__width = size
                self.__height = size
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """
        updates specified attributes
        """
        if len(args) > 0:
            if len(args) >= 1:
                if type(args[0]) == int:
                    self.id = args[0]
                else:
                    raise TypeError("id must be an integer")

                if len(args) >= 2:
                    if type(args[1]) == int:
                        if args[1] > 0:
                            self.__width = args[1]
                            self.__height = args[1]
                        else:
                            raise ValueError("width must be > 0")
                    else:
                        raise TypeError("width must be an integer")

                    if len(args) >= 3:
                        if type(args[2]) == int:
                            if args[2] > 0:
                                self.__x = args[2]
                            else:
                                raise ValueError("x must be > 0")
                        else:
                            raise TypeError("x must be an integer")

                        if len(args) >= 4:
                            if type(args[3]) == int:
                                if args[3] >= 0:
                                    self.__y = args[3]
                                else:
                                    raise ValueError("y must be >= 0")
                            else:
                                raise TypeError("y must be an integer")
        else:
            if 'id' in kwargs:
                if type(kwargs['id']) == int:
                    self.id = kwargs['id']
                else:
                    raise TypeError("id must be an integer")

            if 'size' in kwargs:
                if type(kwargs['size']) == int:
                    if kwargs['size'] > 0:
                        self.__width = kwargs['size']
                        self.__height = kwargs['size']
                    else:
                        raise ValueError("width must be > 0")
                else:
                    raise TypeError("width must be an integer")

            if 'x' in kwargs:
                if type(kwargs['x']) == int:
                    if kwargs['x'] >= 0:
                        self.__x = kwargs['x']
                    else:
                        raise ValueError("x must be >= 0")
                else:
                    raise TypeError("x must be an integer")

            if 'y' in kwargs:
                if type(kwargs['y']) == int:
                    if kwargs['y'] >= 0:
                        self.__y = kwargs['y']
                    else:
                        raise ValueError("y must be >= 0")
                else:
                    raise TypeError("y must be an integer")

    def to_dictionary(self):
        """
        returns dictionary representation of Square
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.__width
        my_dict['x'] = self.__x
        my_dict['y'] = self.__y
        return my_dict