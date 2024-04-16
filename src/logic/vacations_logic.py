from utils.dal import *
from model.users_model import *
from model.vacations_model import * 

class VacationsLogic:
    def __init__(self):
        self.dal = DAL()

    #👍
    def get_all_vacations(self):
        sql = "SELECT * FROM vacation.vacations LIMIt 3"
        result = self.dal.get_table(sql)
        result_to_object = VacationsModel.dictionaries_to_objects(result)
        return result_to_object
    
    #👍
    def insert_new_vacation(self, countryID, description, startDate, endDate, price, vacationPictureFile):
        sql = """
        INSERT INTO vacation.vacations (countryID,description,startDate,endDate,price,vacationPictureFile)
        VALUES  (%s, %s, %s, %s, %s, %s);
        """
        params = (countryID,description,startDate,endDate,price,vacationPictureFile)
        result = self.dal.insert(sql,params)  #returns last_row_id
        if result is not None:
            # Construct SQL query to fetch the newly inserted vacation
            sql_select_new_vacation = "SELECT * FROM vacation.vacations WHERE vacationID = %s"
            new_vacation = self.dal.get_table(sql_select_new_vacation, (result,))
            return f"Last row id: {result}\nNew Vacation Added: {new_vacation}"
        else:
            return "No rows inserted"
    
    def close(self):
        self.dal.close()