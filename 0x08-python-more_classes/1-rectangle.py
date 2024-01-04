#!/usr/bin/python3

"""
Rectangle module.
Defines a rectangle.
"""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
