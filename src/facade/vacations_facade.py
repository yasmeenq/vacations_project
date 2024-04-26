from utils.dal import *
from model.vacations_model import *
from logic.vacations_logic import *
from datetime import datetime

class VacationsFacade:
    def __init__(self):
        self.logic = VacationsLogic()

    # get all vacations 
    def get_vacations_sorted_by_date_desc(self):   
        vacations = self.logic.get_all_vacations()
        return vacations

    # add new vacation 
    def add_new_vacation(self,countryID, description, startDate, endDate,price, vacationPictureFile):
        
        #1) all fields connot be empty:
        while not countryID:
            print("countryID cannot be empty.")
            countryID = input("enter countryID: ")
        
        while not description:
            print("description cannot be empty.")
            description = input("enter description: ")
        
        while not startDate:
            print("startDate cannot be empty.")
            startDate = input("enter startDate: ")

        while not endDate:
            print("endDate cannot be empty.")
            endDate = input("enter endDate: ")

        while not price:
            print("price cannot be empty.")
            price = input("enter price: ")

        while not vacationPictureFile:
            print("vacationPictureFile cannot be empty.")
            vacationPictureFile = input("enter vacationPictureFile: ")


        #2) price cannot be negative or more than 10,000: 
        while price < 0:
            print("price cannot be negative. Please try again.")
            price = input("enter price: ")
        while price > 10000:
            print("price cannot be more than 10,000 Please try again.")
            price = input("enter price: ")           

        #3) start date cannot be greater than end date:

        # Convert strings to datetime objects
        start_date = datetime.strptime(startDate, '%Y-%m-%d')
        end_date = datetime.strptime(endDate, '%Y-%m-%d')

        # Compare dates
        if start_date <= end_date:
            return True
        if start_date > end_date:
            return f"start date cannot be greater than end date."
            
        #4) must be valid dates - not from the past:

        try:
            # Convert string to datetime object
            getStartDate = datetime.strptime(startDate, '%Y-%m-%d')
            getEndDate = datetime.strptime(endDate, '%Y-%m-%d')
            # Get current date
            current_date = datetime.now().date()
            # Check if date is not in the past
            if getStartDate.date() >= current_date and getEndDate.date() >= current_date:
                return True
            if getStartDate.date() < current_date or getEndDate.date() < current_date:
                return False
        except ValueError as e:
                return f"Value Error: Invalid Date."


    # new_vacation = vacation_logic.insert_new_vacation(
    #     insert_country_id, insert_description,
    #     insert_startDate, insert_endDate,
    #     insert_price, insert_picture
    #     )
    # print(new_vacation)




    # # update an existing vacation 👍
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
    
    # # delete an existing vacation 👍🤩
    # delete_vacationID = str(input("enter vacation ID you want to delete: "))
    # delete_vacation = vacation_logic.delete_existing_vacation(delete_vacationID)
    # print(delete_vacation)

