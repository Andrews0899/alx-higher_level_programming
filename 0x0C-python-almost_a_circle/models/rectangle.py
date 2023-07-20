#!/usr/bin/python3

'''Rectangle class.'''

from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Rectangle Constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for the width property.

        Args:
            value (int): Width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than or equal to 0.
        '''
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for the height property.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than or equal to 0.
        '''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x-coordinate of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for the x property.

        Args:
            value (int): x-coordinate value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        '''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y-coordinate of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for the y property.

        Args:
            value (int): y-coordinate value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        '''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''
        Validates if a value is an integer and satisfies certain conditions.

        Args:
            name (str): Name of the property.
            value: Value to be validated.
            eq (bool, optional): Indicates if value can be equal to 0. Defaults to True.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value does not satisfy the conditions.
        '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        '''Computes the area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints a string representation of this rectangle.'''
        s = '\n' * self.y + (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''
        Returns a string representation of this rectangle.

        Returns:
            str: String representation of this rectangle.
        '''
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''
        Internal method that updates instance attributes via */**args.

        Args:
            id (int, optional): ID to update. Defaults to None.
            width (int, optional): Width to update. Defaults to None.
            height (int, optional): Height to update. Defaults to None.
            x (int, optional): x-coordinate to update. Defaults to None.
            y (int, optional): y-coordinate to update. Defaults to None.
        '''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''
        Updates instance attributes via no-keyword & keyword args.

        Args:
            *args: Positional arguments to update the attributes.
            **kwargs: Keyword arguments to update the attributes.
        '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''
        Returns a dictionary representation of this class.

        Returns:
            dict: Dictionary representation of this class.
        '''
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
