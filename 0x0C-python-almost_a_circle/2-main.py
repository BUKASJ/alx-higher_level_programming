#!/usr/bin/python3
"""
Module for Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle's top-left corner.
            y (int): The y coordinate of the rectangle's top-left corner.
            id (int): The identifier for the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width or height is not greater than 0, or if x or y is less than 0.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x coordinate of the rectangle's top-left corner.

        Returns:
            int: The x coordinate of the rectangle's top-left corner.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x coordinate of the rectangle's top-left corner.

        Args:
            value (int): The x coordinate of the rectangle's top-left corner.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y coordinate of the rectangle's top-left corner.

        Returns:
            int: The y coordinate of the rectangle's top-left corner.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y coordinate of the rectangle's top-left corner.

        Args:
            value (int): The y coordinate of the rectangle's top-left corner.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
