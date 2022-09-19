#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ This is a Rectangle Class (it defines a rectangle) """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Instantiation of rectangle with width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ returns width of Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width of Rectangle """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ returns height of Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height of Rectangle """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of Rectangle """
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = self.__width * 2 + self.__height * 2
        return p

    def __str__(self):
        """returns representation of rectangle with print_symbol"""
        s = ''
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                s += str('#' * self.width) + '\n'
        return s[:-1]

    def __repr__(self):
        """returns string representation of Rectangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """detects deletion of Rectangle"""
        Rectangle.number_of_instances -= 1
        return print('Bye rectangle...')
