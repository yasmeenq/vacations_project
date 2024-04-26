from utils.dal import *
from model.vacations_model import *
from logic.vacations_logic import *
from datetime import datetime

class VacationsFacade:
    def __init__(self):
        self.logic = VacationsLogic()


    def get_vacations_sorted_by_date_desc(self):
        print("\nAll vacations: ")   
        vacations = self.logic.get_all_vacations()
        return vacations


    def add_new_vacation(self, countryID, description, startDate, endDate, price, vacationPictureFile):
        
        # Input validation - cannot have empty fields
        if not all([countryID, description, startDate, endDate, price, vacationPictureFile]):
            return "Fields cannot be empty. Please try again."

        # Validate countryID - must be integer
        try:
            countryID = int(countryID)
        except ValueError:
            return "CountryID must be an integer."
        
        # Validate price - cannot be negative or over 10,000
        try:
            price = float(price)
            if not 0 <= price <= 10000:
                return "Price must be between 0 and 10,000."
        except ValueError:
            return "Price must be a valid number."       

        # Validate dates
        try:
            # Convert date string to datetime object
            getStartDate = datetime.strptime(startDate, '%Y-%m-%d')
            getEndDate = datetime.strptime(endDate, '%Y-%m-%d')
            
            if getStartDate > getEndDate:
                return "Start date cannot be greater than end date."

            # Get current date
            current_date = datetime.now().date()

            if getStartDate.date() < current_date or getEndDate.date() < current_date:
                return "Invalid Date: Dates cannot be in the past."
        
        except ValueError:
            return "Invalid Date Format. Date must be in YYYY-MM-DD format."
        
        # Add Vacation
        new_vacation = self.logic.insert_new_vacation(countryID, description, startDate, endDate, price, vacationPictureFile)
        return new_vacation


    def update_vacation(self, vacationID, countryID, description, startDate, endDate,price, vacationPictureFile):
        
        # Input validation - cannot have empty fields except for vacation picture.
        if not all([vacationID, countryID, description, startDate, endDate, price]):
            return "All Fields must be filled except for vacation picture. Please try again."
        
        # Validate vacationID and countryID - must be integers
        try:
            vacationID = int(vacationID)
            countryID = int(countryID)
        except ValueError:
            return "VacationID and CountryID must be integers."

        # Validate price - cannot be negative or over 10,000
        try:
            price = float(price)
            if not 0 <= price <= 10000:
                return "Price must be between 0 and 10,000."
        except ValueError:
            return "Price must be a valid number."    

        # Validate dates
        try:
            getStartDate = datetime.strptime(startDate, '%Y-%m-%d')
            getEndDate = datetime.strptime(endDate, '%Y-%m-%d')

            if getStartDate > getEndDate:
                return "Start date cannot be greater than end date."
            
        except ValueError:
            return "Invalid Date Format. Date must be in YYYY-MM-DD format."

        # Update Vacation
        update_vacation = self.logic.update_existing_vacation(vacationID, countryID, description, startDate, endDate,price, vacationPictureFile)
        return update_vacation
    

    def delete_vacation(self, vacationID):      
        try:
            vacationID = int(vacationID)
        except ValueError:
            return "VacationID must be an integer."
        
        delete_vacation = self.logic.delete_existing_vacation(vacationID)
        return delete_vacation

    def close(self):
        self.logic.close()