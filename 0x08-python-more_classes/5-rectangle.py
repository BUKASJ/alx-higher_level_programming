#!/usr/bin/python3
""" Rectangle Module! For rectangular purposes only. """


class Rectangle:
    """ Rectangle class! For rectangles ONLY. """
    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height

    # method returns the string representation of the object
    def __str__(self):
        """ string conversion """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    # function returns the object representation
    def __repr__(self):
        """ string conversion """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ method is a known as a destructor """
        # called when an object gets destroyed
        print("Bye rectangle...")

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width + self.__height) * 2
