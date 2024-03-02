#!usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        name = obj.__class__.__name__
        self.__objects[f"{name}.{obj.id}"] = obj

    def save(self):
        """ Serializes __objects to the JSON file """

       file = self.__file_path
        objd = self.__objects
        s_obj = {}
        for key, value in objd.items():
            s_obj[key] = value.to_dict()

        with open(file, "w") as f:
            json.dump(s_obj, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """

       file = self.__file_path

        try:
            with open(file, "r") as f:
                data = json.load(f)
            for key in data:
                class_name = key.split('.')[0]
                self.__objects[key] = eval(f"{class_name}(**data[key])")
        except FileNotFoundError:
            pass
