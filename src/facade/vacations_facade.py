from utils.dal import *
from model.vacations_model import *
from logic.vacations_logic import *


vacation_logic = VacationsLogic()

# get all vacations 👍
all_vacations = vacation_logic.get_all_vacations()
for vacation in all_vacations:
    print(vacation)
print()

# add new vacation 👍
insert_country_id = str(input("insert countryID: "))
insert_description = input("insert description: ")
insert_startDate = input("insert startDate: ")
insert_endDate = input("insert endDate: ")
insert_price = input("insert price: ")
insert_picture = input("insert vacation picture file: ")

new_vacation = vacation_logic.insert_new_vacation(
    insert_country_id, insert_description,
    insert_startDate, insert_endDate,
    insert_price, insert_picture
    )
print(new_vacation)

# update an existing vacation 👍
update_vacation_id = str(input("enter vacation ID you want to update: "))
update_country_id = str(input("update countryID: "))
update_description = input("update description: ")
update_startDate = input("update startDate: ")
update_endDate = input("update endDate: ")
update_price = input("update price: ")
update_picture = input("update vacation picture file: ")

updated_vacation = vacation_logic.update_existing_vacation(
    update_vacation_id, update_country_id,update_description,
    update_startDate, update_endDate,
    update_price, update_picture
    )
print(updated_vacation)
 
# delete an existing vacation 👍🤩
delete_vacationID = str(input("enter vacation ID you want to delete: "))
delete_vacation = vacation_logic.delete_existing_vacation(delete_vacationID)
print(delete_vacation)

