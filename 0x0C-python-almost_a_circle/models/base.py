#!/usr/bin/python3
"""Base Class Module"""
import json
import csv
import turtle


class Base:
    """Base Class to manage id attribute"""
    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string static method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string static method"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw static method"""
        if type(list_rectangles) == list and type(list_squares) == list:
            turtle.screensize(500, 500)
            x = -150
            y = 150
            for r in list_rectangles:
                turtle.pu()
                turtle.setpos(x, y)
                turtle.pd()
                for i in range(2):
                    turtle.forward(r.width)
                    turtle.right(90)
                    turtle.forward(r.height)
                    turtle.right(90)
                x += 300
            y *= -1
            x -= 300
            for s in list_squares:
                turtle.pu()
                turtle.setpos(x, y)
                turtle.setheading(180)
                turtle.pd()
                for i in range(4):
                    turtle.forward(s.size)
                    turtle.right(90)
                x -= 250

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(Base.to_json_string([]))
        else:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(Base.to_json_string([x.to_dictionary()
                                             for x in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """create class method"""
        if type(dictionary) == dict:
            if cls.__name__ == "Rectangle":
                retcls = cls(1, 1)
            elif cls.__name__ == "Square":
                retcls = cls(1)
            retcls.update(**dictionary)
            return retcls

    @classmethod
    def load_from_file(cls):
        """load_from_file method"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                objl = cls.from_json_string(f.read())
            return [cls.create(**d) for d in objl]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv method"""
        if list_objs is None:
            list_objs = []
        if cls.__name__ == "Rectangle":
            with open(cls.__name__ + ".csv", "w+") as f:
                RectAttr = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(f, RectAttr)
                writer.writeheader()
                for o in list_objs:
                    writer.writerow(o.to_dictionary())
        elif cls.__name__ == "Square":
            with open(cls.__name__ + ".csv", "w+") as f:
                SqAttr = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, SqAttr)
                writer.writeheader()
                for o in list_objs:
                    writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        with open(cls.__name__ + ".csv") as f:
            objl = []
            retl = []
            reader = csv.DictReader(f)
            for row in reader:
                objl.append(row)
            for o in objl:
                for key in o.keys():
                    o[key] = int(o[key])
            for d in objl:
                retl.append(cls.create(**d))
            return retl

    def __init__(self, id=None):
        """init magic method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
