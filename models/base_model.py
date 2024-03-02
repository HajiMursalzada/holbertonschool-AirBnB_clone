#!/usr/bin/python3

"""Base Model"""

import uuid
from datetime import datetime
"""from models import storage"""

class BaseModel:
    """Class"""
    def __init__(self, *args, **kwargs):
        """Initialize Instance Attributes"""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                     self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
           """ storage.new(self)"""

    def __str__(self):
        """Str Method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save Method"""
        self.updated_at = datetime.now()
       """ storage.save()"""

    def to_dict(self):
        """Dict Method"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
