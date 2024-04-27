from utils.dal import *
from model.vacations_model import *
from logic.vacations_logic import *
from datetime import datetime

class VacationsFacade:
    
    def __init__(self):
        self.logic = VacationsLogic()

    #👍
    def get_vacations_sorted_by_date_desc(self):
        vacations = self.logic.get_all_vacations()
        for item in vacations:
            print(item)

    @staticmethod 
    def validate_price(price):
        return 0 <= float(price) <= 10000

    @staticmethod 
    def validate_dates(startDate, endDate):
        try:
            # Convert date string to datetime object
            start_date = datetime.strptime(startDate, '%Y-%m-%d')
            end_date = datetime.strptime(endDate, '%Y-%m-%d')

            # Check if start date is before end date
            if start_date > end_date:
                raise ValueError("Start date cannot be greater than end date.")
        
        except ValueError as e:
            raise ValueError("Invalid Date Format. Date must be in YYYY-MM-DD format.")


    #👍
    def add_new_vacation(self, countryID, description, startDate, endDate, price, vacationPictureFile):
        
        # Input validation - cannot have empty fields
        if not all([countryID, description, startDate, endDate, price, vacationPictureFile]):
            raise ValueError("Fields cannot be empty. Please try again.")

        # Validate countryID - must be integer
        if not isinstance(countryID, int):
            raise ValueError("CountryID must be an integer.")
        
        # Validate price - cannot be negative or over 10,000
        if not self.validate_price(price):
            raise ValueError("Price must be a valid number between 0 and 10,000")  

        # Validate dates
        self.validate_dates(startDate, endDate)

        # Check if dates are in the past
        start_date = datetime.strptime(startDate, '%Y-%m-%d')
        end_date = datetime.strptime(endDate, '%Y-%m-%d')
        current_date = datetime.now().date()
        if start_date.date() < current_date or end_date.date() < current_date:
            raise ValueError("Dates cannot be in the past.")
        
        # Add Vacation
        new_vacation = self.logic.insert_new_vacation(countryID, description, startDate, endDate, price, vacationPictureFile)
        return new_vacation

    #👍
    def update_vacation(self, vacationID, countryID, description, startDate, endDate,price, vacationPictureFile):
        
        # Input validation - cannot have empty fields except for vacation picture.
        if not all([vacationID, countryID, description, startDate, endDate, price]):
            raise ValueError("All Fields must be filled except for vacation picture. Please try again.")
        
        # Validate vacationID and countryID - must be integers
        if not isinstance(vacationID, int) or not isinstance(countryID, int):
            raise ValueError("VacationID and CountryID must be integers.")

        # Does vacation exist to update it?
        does_vacation_exist = self.logic.get_one_vacation(vacationID)
        if not does_vacation_exist:
            raise ValueError("Vacation doesn't exist. try again.")

        # Validate price - cannot be negative or over 10,000
        if not self.validate_price(price):
            raise ValueError("Price must be a valid number between 0 and 10,000")  
 
        # Validate dates
        self.validate_dates(startDate, endDate)

        # Update Vacation
        update_vacation = self.logic.update_existing_vacation(vacationID, countryID, description, startDate, endDate,price, vacationPictureFile)
        return update_vacation
    

    def delete_vacation(self, vacationID): 

        # Validate vacationID - must be int
        if not isinstance(vacationID, int):
            raise ValueError("VacationID must be an integer.")     
        
        # Delete Vacation
        delete_vacation = self.logic.delete_existing_vacation(vacationID)
        return delete_vacation

    def close(self):
        self.logic.close()