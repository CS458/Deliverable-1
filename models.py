import re
import os
import json
import sys
from settings.config import DATABASE_DIR


class User:
    def __init__(self, identifier):
        self.phone = self.email = None
        phone_match = re.match(r'^(\+\d{1,2}\s?)?((\(\d{3}\))|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$', identifier)
        email_match = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', identifier)
        
        if phone_match:
            self.phone = identifier
        
        elif email_match:
            self.email = identifier
    
    @property
    def is_valid(self):
        if self.email or self.phone:
            return True
        
        return False
    
    @property
    def __user(self):
        if not self.is_valid:
            return None
        
        with open(os.path.join(DATABASE_DIR, "user.json")) as file:
            users = json.load(file)

        if self.email:
            for user in users:
                if user["email"] == self.email:
                    return user
                
        elif self.phone:
            for user in users:
                if user["phone"] == self.phone:
                    return user
                
        return None
    
    @property
    def id(self):
        if not self.is_valid:
            return False
        
        if not self.__user: #
            return False

        return self.__user["id"]

    def verify(self, not_hashed_password):
        if not self.is_valid:
            return False
        
        if not self.__user: #
            return False

        if self.__user["password"] == not_hashed_password:
            return True
        
        return False
        



