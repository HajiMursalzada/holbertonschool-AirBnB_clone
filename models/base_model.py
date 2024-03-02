#!/usr/bin/python3

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ Base Class """
    
    def __init__(self, *args, **kwargs):
        """ Initilize Instance """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns dictionary representation """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance """

        obj_dict = self.__dict__.copy()
        obj_dict.update(__class__=self.__class__.__name__)
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
