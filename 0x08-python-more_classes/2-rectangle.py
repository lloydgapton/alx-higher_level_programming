#!/usr/bin/python3
"""A module for a rectangle class"""


class Rectangle:
    """Init class width set 0 and height set 0"""
    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self._height = height

    @property
    def width(self):
        """ Width Getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must eb >= 0")
        self.__height = value

    def area(self):
        """calculate Area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """clculate Perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))
