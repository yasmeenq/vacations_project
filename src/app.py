from utils.dal import *
from model.users_model import *
from model.vacations_model import *
from logic.users_logic import *
from logic.vacations_logic import *
from logic.likes_logic import *


# print("---------------------------------------------------------------------------")
users_logic = UsersLogic()

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

#Check if email exits 🤔
# check_email = input("enter email to check: ")
# checking_output = users_logic.if_email_exist(check_email.strip())
# print(checking_output)

# print("---------------------------------------------------------------------------")
vacation_logic = VacationsLogic()

#get all vacations 👍
# all_vacations = vacation_logic.get_all_vacations()
# for vacation in all_vacations:
#     print(vacation)
# print()

#add new vacation 👍
# insert_country_id = str(input("insert countryID: "))
# insert_description = input("insert description: ")
# insert_startDate = input("insert startDate: ")
# insert_endDate = input("insert endDate: ")
# insert_price = input("insert price: ")
# insert_picture = input("insert vacation picture file: ")

# new_vacation = vacation_logic.insert_new_vacation(
#     insert_country_id, insert_description,
#     insert_startDate, insert_endDate,
#     insert_price, insert_picture
#     )
# print(new_vacation)

#update an existing vacation 👍
# update_vacation_id = str(input("enter vacation ID you want to update: "))
# update_country_id = str(input("update countryID: "))
# update_description = input("update description: ")
# update_startDate = input("update startDate: ")
# update_endDate = input("update endDate: ")
# update_price = input("update price: ")
# update_picture = input("update vacation picture file: ")

# updated_vacation = vacation_logic.update_existing_vacation(
#     update_vacation_id, update_country_id,update_description,
#     update_startDate, update_endDate,
#     update_price, update_picture
#     )
# print(updated_vacation)
 
#delete an existing vacation 👍🤩
# delete_vacationID = str(input("enter vacation ID you want to delete: "))
# delete_vacation = vacation_logic.delete_existing_vacation(delete_vacationID)
# print(delete_vacation)


print("---------------------------------------------------------------------------")

likes_logic = LikesLogic()

#like a vacation 🤔
print("Like a Vacation: ")
user_id_likes = str(input("userID: "))
vacation_id_likes = str(input("vacationID: "))

add_like = likes_logic.add_like(user_id_likes, vacation_id_likes)
print(add_like)
print()
#delete a like of a vacation 🤔
print("Unlike a Vacation: ")
user_id_delete_like = str(input("userID: "))
vacation_id_delete_like = str(input("vacationID: "))

delete_like = likes_logic.delete_like(user_id_delete_like, vacation_id_delete_like)
print(delete_like)

