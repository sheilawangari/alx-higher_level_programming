#!/usr/bin/python3
"""
retangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class which inherits from base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes Rectangle instance
        """
        super().__init__(id)
        self.id = self.id

        if type(width) == int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

        if type(x) == int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

        if type(y) == int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        """
        returns value of width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets value of width
        """
        if type(width) == int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        returns value of height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets value of height
        """
        if type(height) == int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        returns value of x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        sets value of x
        """
        if type(x) == int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """
        returns value of y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        sets value of y
        """
        if type(y) == int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        return area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        print width number and height number of '#'
        """
        res = ""
        for row in range(self.__y - 1):
            print("\n")
        for row in range(self.__height):
            res += (" " * self.__x) + ("#" * self.__width) + "\n"
        print(res[:-1])

    def __str__(self):
        """
        print string
        """
        result1 = "[Rectangle] (" + str(self.id) + ") "
        result2 = str(self.__x) + "/" + str(self.__y) + " - "
        result3 = str(self.__width) + "/" + str(self.__height)
        return result1 + result2 + result3

    def update(self, *args, **kwargs):
        """
        updates values
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
                        else:
                            raise ValueError("width must be > 0")
                    else:
                        raise TypeError("width must be an integer")

                    if len(args) >= 3:
                        if type(args[2]) == int:
                            if args[2] > 0:
                                self.__height = args[2]
                            else:
                                raise ValueError("height must be > 0")
                        else:
                            raise TypeError("height must be an integer")

                        if len(args) >= 4:
                            if type(args[3]) == int:
                                if args[3] >= 0:
                                    self.__x = args[3]
                                else:
                                    raise ValueError("x must be >= 0")
                            else:
                                raise TypeError("x must be an integer")

                            if len(args) >= 5:
                                if type(args[4]) == int:
                                    if args[4] >= 0:
                                        self.__y = args[4]
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

            if 'width' in kwargs:
                if type(kwargs['width']) == int:
                    if kwargs['width'] > 0:
                        self.__width = kwargs['width']
                    else:
                        raise ValueError("width must be > 0")
                else:
                    raise TypeError("width must be an integer")

            if 'height' in kwargs:
                if type(kwargs['height']) == int:
                    if kwargs['height'] > 0:
                        self.__height = kwargs['height']
                    else:
                        raise ValueError("height must be > 0")
                else:
                    raise TypeError("height must be an integer")

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
        returns dictionary representation of Rectangle
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.__width
        my_dict['height'] = self.__height
        my_dict['x'] = self.__x
        my_dict['y'] = self.__y
        return my_dict
        