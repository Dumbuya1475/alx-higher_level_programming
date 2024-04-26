#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
<<<<<<< HEAD
        return self._width
=======
        return self.__width
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
<<<<<<< HEAD
        self._width = value
=======
        self.__width = value
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
<<<<<<< HEAD
        return self._height
=======
        return self.__height
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
<<<<<<< HEAD
        self._height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self._width * self._height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return (0)
        return ((self._width * 2) + (self._height * 2))
=======
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
