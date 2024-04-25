from utils.dal import *
from model.users_model import *
from logic.users_logic import *
import re

class UsersFacade:
    def __init__(self):
        self.logic= UsersLogic()

    # register a new user:
    def user_registration(self, firstName, lastName, email, password):
        print("Welcome! Please fill in all the following fields to register as a new user 😊")

        #1) make sure all fields are not empty:

        while not firstName.strip():  # Check if the input is empty(not true) or contains only whitespace
            print("firstName cannot be empty.")
            firstName = input("Enter first name: ")

        while not lastName.strip(): 
            print("lastName cannot be empty.")
            lastName = input("Enter last name: ")

        while not email.strip():  
            print("email cannot be empty.")
            email = input("Enter email: ")

        while not str(password).strip():
            print("password cannot be empty.")
            password = input("Enter password: ")


        #2) make sure email is valid:

        # Regular expression pattern for validating email addresses
        pattern = r'^[\w\.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
            
        # Check if the email matches the pattern
        while not re.match(pattern, email):
            print("Email is not valid. Please try again.")
            email = input("Enter email: ")

        #3) password must be minimum 4 characters:
        while len(str(password).strip()) < 4:
            print("Password must be minimum 4 characters. please try again")
            password = input("Enter password: ")

        #4) email already exists:
        while self.logic.if_email_exist(email) == "Email Exists ✔":
            print("Email already exists. Please choose another one.")
            email = input("Enter email: ")

        #5) adding a new user
        new_user = self.logic.add_regular_user(firstName, lastName, email, password)
        
        return new_user
    
    print("==================================================================================")
    
    def user_login(self, email, password):
        # Check if email and password are provided
        if not email.strip() or not str(password).strip():
            return "Email and password cannot be empty."

        # Validate email format
        pattern = r'^[\w\.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return "Email is not valid. Please try again."

        # Validate password length
        if len(str(password).strip()) < 4:
            return "Password must be minimum 4 characters. Please try again."


        # Check if the user exists
        check_user = self.logic.get_user_by_email_password(email, password)

        if check_user == "User Doesn't Exist.":
            # If user doesn't exist, check if the email exists
            check_email = self.logic.if_email_exist(email)
            
            if check_email == "Email Doesn't Exist ✖":
                return "Incorrect Email. Please try again."
            elif check_email == "Email Exists ✔":
                return "Incorrect Password. Please try again."
        else:
            # If the user exists, extract and return the user information
            if isinstance(check_user, list) and len(check_user) > 0:
                user_info = check_user[0]
                return f"Logged in successfully. \n{user_info}"
            else:
                return "User Doesn't Exist."
                
        return None
        
    
    def close(self):
        self.logic.close()    




