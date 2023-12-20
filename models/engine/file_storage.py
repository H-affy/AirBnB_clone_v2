#!/usr/bin/python3
"""defines the file storage  class."""
from models.base_model import BaseModel
import json
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class FileStorage:
    """represents an abstract storage engine.

    Attributes:
    __file_path (str): Name of the file to save objects to
    __objects (dict): Dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary"""
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """set in __objects obj with key <obj_class_name>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """delete an existing element"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """calls reload()"""
        self.reload()
