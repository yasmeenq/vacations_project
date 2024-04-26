from utils.dal import *
from model.users_model import *
from logic.users_logic import *
import re

class UsersFacade:
    def __init__(self):
        self.logic= UsersLogic()

    @staticmethod
    def validate_email(email):
        # Regular expression pattern for validating email addresses
        pattern = r'^[\w\.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    @staticmethod
    def validate_password(password):
        return len(str(password).strip()) >= 4


    def user_registration(self, firstName, lastName, email, password):
        # Input validation - cannot have empty fields
        if not all([firstName, lastName, email, password]):
            return "Fields cannot be empty. Please try again."

        # Validate email format
        if not self.validate_email(email):
            return "Email is not valid. Please try again."
            
        # Validate password - must be minimum of 4 characters
        if not self.validate_password(password):
            return "Password must be minimum 4 characters. Please try again."

        # Validate if email exists:
        if self.logic.if_email_exist(email) == "Email Exists ✔":
            return "Email already exists. Please choose another one."

        # Register User:
        new_user = self.logic.add_regular_user(firstName, lastName, email, password)
        return f"{new_user} \nregistered successfully! Welcome!😊"
    
    
    def user_login(self, email, password):
        # Input validation - cannot have empty fields
        if not email.strip() or not str(password).strip():
            return "Email and password cannot be empty."

        # Validate email format:
        if not self.validate_email(email):
            return "Email is not valid. Please try again."

        # Validate password - must be minimum of 4 characters
        if not self.validate_password(password):
            return "Password must be minimum 4 characters. Please try again."

        # Check if the user exists
        check_user = self.logic.get_user_by_email_password(email, password)

        if check_user == "User Doesn't Exist.":
            return "Incorrect Email or Password. Please try again."
        elif isinstance(check_user, list) and len(check_user) > 0:
            return f"Logged in successfully.\n{check_user[0]}"
        else:
            return "User Doesn't Exist."
                
    
    def close(self):
        self.logic.close()    




