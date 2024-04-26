#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
<<<<<<< HEAD
=======
        print_symbol (any): The symbol used for string representation.
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
<<<<<<< HEAD
        if self._width == 0 or self._height == 0:
            return ("")

        rct = []
        for i in range(self._height):
            [rct.append('#') for j in range(self._width)]
            if i != self._height - 1:
                rct.append("\n")
        return ("".join(rct))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rct = "Rectangle(" + str(self._width)
        rct += ", " + str(self._height) + ")"
        return (rct)
=======
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
<<<<<<< HEAD

=======
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
