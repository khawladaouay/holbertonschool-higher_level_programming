#!/usr/bin/python3
"""Define Base class"""
import json
from os import path
import csv


class Base:
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file: writes the json string representation of list_objs"""
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([o.to_dictionary()
                        for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances"""
        file_name = cls.__name__ + '.json'
        if path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                dictionary = cls.from_json_string(f.read())
            return[cls.create(**obj) for obj in dictionary]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        my_list = []
        new_list = []
        for elem in list_objs:
            my_dict = elem.to_dictionary()
            for value in my_dict.values():

                new_list.append(value)
            my_list.append(new_list[:])
            new_list = []

        with open(filename, "w", encoding="utf-8") as my_file:
            writer = csv.writer(my_file)
            writer.writerows(my_list)

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        my_objects = []
        my_attr_rectangle = ["id", "width", "height", "x", "y"]
        my_attr_square = ["id", "size", "x", "y"]

        if not path.exists(filename):
            return my_objects

        with open(filename, mode="r", encoding="utf-8") as my_file:
            csv_reader = csv.reader(my_file)
            for line in csv_reader:

                if cls.__name__ == "Rectangle":
                    my_dict = {}
                    for i in range(len(line)):
                        my_dict[my_attr_rectangle[i]] = int(line[i])
                    my_objects.append(cls.create(**my_dict))

                if cls.__name__ == "Square":
                    my_dict = {}
                    for j in range(len(line)):
                        my_dict[my_attr_square[j]] = int(line[j])
                    my_objects.append(cls.create(**my_dict))

        return my_objects