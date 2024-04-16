from utils.dal import *
from model.users_model import *
from model.vacations_model import * 

class UsersLogic:
    def __init__(self):
        self.dal = DAL()

    #👍
    def get_all_users(self):
        sql = "SELECT * FROM vacation.users"
        result = self.dal.get_table(sql)
        result_to_obj = UsersModel.dictionaries_to_objects(result)
        return result_to_obj
   
   #👍
    def get_one_user(self):
        sql = "SELECT * FROM vacation.users"
        result = self.dal.get_one_row(sql)
        result_to_obj = UsersModel.dictionary_to_object(result)
        return result_to_obj

    #👍
    def add_regular_user(self,firstname,lastname,email,password):
        sql = """
        INSERT INTO vacation.users
        (firstname, lastname, email, password, roleID) 
        VALUES (%s, %s, %s, %s, 2)
        """
        params = (firstname,lastname,email,password)
        result = self.dal.insert(sql, params)

        if result is not None:
            # Construct SQL query to fetch the newly inserted user
            sql_select_new_user = "SELECT * FROM vacation.users WHERE userID = %s"
            new_user = self.dal.get_table(sql_select_new_user, (result,))
            return f"Last row id: {result}\nNew user: {new_user}"
        else:
            return "No rows inserted"

    #👍
    def get_user_by_email_password(self, email, password):
        sql = f"SELECT * FROM vacation.users WHERE email = %s AND password= %s"
        params = (email,password)
        result = self.dal.get_table(sql, params)
        if not result:  # Check if the result set is empty
            return "User Doesn't Exist."
        else:
            result_to_obj = UsersModel.dictionaries_to_objects(result)
            return result_to_obj 

    #👍
    def if_email_exist(self,email):
        sql = f"SELECT * FROM vacation.users WHERE email = %s"
        params = (email,)
        result = self.dal.get_table(sql, params)
        if not result:  # Check if the result set is empty
            return "Email Doesn't Exist ✖"
        else:
            return "Email Exists ✔"

    def close(self):
        self.dal.close()

