#!/usr/bin/python3

'''Base Class Module.'''
from json import dumps, loads
import csv


class Base:
    '''Our OOP representation.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Base Class Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON representation of the list of dictionaries.
        '''
        if not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        '''
        return loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects.

        Returns:
            None
        '''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        '''
        Loads a list of objects from a JSON file.

        Args:
            None

        Returns:
            list: List of objects.
        '''
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        '''
        Creates an instance of a class from a dictionary.

        Args:
            **dictionary: Dictionary containing the attributes of the object.

        Returns:
            Instance of the class.
        '''
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            new_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            from models.square import Square
            new_instance = Square(1)
        else:
            new_instance = None
        if new_instance:
            new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Saves a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects.

        Returns:
            None
        '''
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        '''
        Loads a list of objects from a CSV file.

        Args:
            None

        Returns:
            list: List of objects.
        '''
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                return [cls.create(**cls.csv_row_to_dict(row)) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Draws a visualization of rectangles and squares using Turtle.

        Args:
            list_rectangles (list): List of Rectangle objects.
            list_squares (list): List of Square objects.

        Returns:
            None
        '''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for obj in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((obj.x + t.pos()[0], obj.y - t.pos()[1]))
            t.pensize(10)
            for _ in range(2):
                t.forward(obj.width)
                t.left(90)
                t.forward(obj.height)
                t.left(90)
            t.end_fill()

        time.sleep(5)
