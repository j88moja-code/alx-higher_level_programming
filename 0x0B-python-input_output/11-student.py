#!/usr/bin/python3
"""Class Student that defines a student
"""


class Student:
    """ New class of student
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        flag = 0
        if isinstance(attrs, list):
            for string in attrs:
                if isinstance(string, str) is False:
                    flag = 1
        else:
            flag = 1

        if flag:
            return self.__dict__
        else:
            new_dict = {}
            for string in attrs:
                if string in self.__dict__:
                    new_dict[string] = self.__dict__[string]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        """
        for attrs in json:
            setattr(self, attrs, json[attrs])
