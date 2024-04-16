from utils.dal import *
from model.users_model import *
from model.vacations_model import *
from logic.users_logic import *
from logic.vacations_logic import *

# users_logic = UsersLogic()

# # print all users 👍
# all_users = users_logic.get_all_users()
# print("All Users:")
# for user in all_users:
#     print(user)
# print()

#get one user  👍
# one_user = users_logic.get_one_user()
# print(f"One User:\n{one_user}")
# print() 

# add a regular user roleId= 2 (not admin) 👍
# print("Add new user details:")
# new_firstname = input("first name: ")
# new_lastname = input("last name: ")
# new_email = input("email: ")
# new_password= input("password: ")
# print()
# r = users_logic.add_regular_user(new_firstname, new_lastname, new_email, new_password)
# print(r)


#get user by email and password 👍
# user_email = input("email: ")
# user_password = input("password: ")
# name_output = users_logic.get_user_by_email_password(user_email, user_password)
# if isinstance(name_output, str):  # Check if the output is a string
#     print(name_output)  #in case user doesn't exist
# else:
#     for item in name_output:
#         print(item)

#Check if email exits 
# check_email = input("enter email to check: ")
# checking_output = users_logic.if_email_exist(check_email.strip())
# print(checking_output)

print("---------------------------------------------------------------------------")
vacation_logic = VacationsLogic()

# #get all vacations 👍
all_vacations = vacation_logic.get_all_vacations()
for vacation in all_vacations:
    print(vacation)
print()

#add new vacation 👍
new_vacation = vacation_logic.insert_new_vacation(5, "aaa", "2024-01-01", "2024-01-11", 7000.00, "stam.png")
print(new_vacation)