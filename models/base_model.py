#!/usr/bin/python3

"""Base Model"""

import uuid
from datetime import datetime

class BaseModel:
    """Class"""
    def __init__(self):
        """Initialize Instance Attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Str Method"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save Method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dict Method"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
