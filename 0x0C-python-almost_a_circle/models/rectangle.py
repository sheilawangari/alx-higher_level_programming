#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class the inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        # Check that value is a valid interger
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        # Check that value is a vali integer
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        # check that value is a valid integer
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return self.y

    @y.setter
    def y(self, value):
        # check that value is a valid integer
        if type(value) != int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of a Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints a rep of the rectangle with a # in stdout"""
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string rep of a rectangle object"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - " + 
                f"{self.width}/{self.height}")
                


