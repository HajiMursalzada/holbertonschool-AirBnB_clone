#!/usr/bin/python3
"""FileStorage class"""

import json

class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances """

     __file_path = "file.json"
     __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        
        return self.__objects
    
    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """ Serializes __objects to the JSON file """
        
        serialized_object = {}
        for key, value in self.__objects.items():
            serialized_object[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_object, f)

    def reload(self):
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                for key, value in json.load(f).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
