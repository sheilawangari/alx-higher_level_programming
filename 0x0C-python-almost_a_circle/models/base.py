#!/usr/bin/python3
"""base module"""


class Base:
    """
    Base class from which all other classes will be derived.
    ...
    Attributes
    ----------
    __nb_objects : int
        global variable for number of instances
    Methods
    -------
    to_json_string(list_dictionaries)
        returns JSON string representation of list_dictionaries, \
                returns "[]" if list_dictionaries is None
    save_to_file(cls, list_objs)
        writes the JSON string representation of list_objs to a file
    """

    global __nb_objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        global __nb_objects
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        import json

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        pass
    