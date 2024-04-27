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
        return re.match(pattern, email.strip())

    @staticmethod
    def validate_password(password):
        return len(str(password).strip()) >= 4

    #👍
    def user_registration(self, firstName, lastName, email, password):

        # Input validation - cannot have empty fields
        if not all([firstName, lastName, email, password]):
            raise ValueError("Fields cannot be empty. Please try again.")
        
        # Check if firstName and lastName are strings
        if not (isinstance(firstName, str) and isinstance(lastName, str)):
            raise ValueError("First name and last name must be strings.")

        # Check if firstName and lastName contain only letters
        if not (firstName.strip().isalpha() and lastName.strip().isalpha()):
            raise ValueError("First name and last name must contain only letters.")

        # Validate email format
        if not self.validate_email(email):
            raise ValueError("Email is not valid. Please try again.")
            
        # Validate password - must be minimum of 4 characters
        if not self.validate_password(password):
            raise ValueError("Password must be minimum 4 characters. Please try again.")

        # Validate if email exists:
        if self.logic.if_email_exist(email) == "Email Exists ✔":
            return "Email already exists. Please choose another one."

        # Register User:
        new_user = self.logic.add_regular_user(firstName, lastName, email, password)
        return f"{new_user} \nRegistered successfully! Welcome {firstName}!😊"
       

   
    #👍
    def user_login(self, email, password):
        # Input validation - cannot have empty fields
        if not all([email, password]):
            raise ValueError("Email and password cannot be empty.")

        # Validate email format:
        if not self.validate_email(email):
            raise ValueError("Email is not valid. Please try again.")

        # Validate password - must be minimum of 4 characters
        if not self.validate_password(password):
            raise ValueError("Password must be minimum 4 characters. Please try again.")

        # Check if the user exists
        try:
            check_user = self.logic.get_user_by_email_password(email, password)

            if check_user == "User Doesn't Exist.":
                return "Incorrect Email or Password. Please try again."
            elif isinstance(check_user, list) and len(check_user) > 0:
                return f"Logged in successfully!\n{check_user[0]}"
            
            else:
                return "User Doesn't Exist. Please try again later."
            
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}. Please try again later."        
                
    
    def close(self):
        self.logic.close()    




