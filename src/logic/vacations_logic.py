from utils.dal import *
from model.vacations_model import * 

# start dal - get vac - insert vac - update vac - delete vac - close dal - #6


class VacationsLogic:
    def __init__(self):
        self.dal = DAL()

    #👍
    def get_all_vacations(self):
        sql = "SELECT * FROM vacation.vacations ORDER BY startDate DESC"
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
        
    #update an existing vacation 👍
    def update_existing_vacation(self, vacationID, countryID, description, startDate, endDate, price, vacationPictureFile):
        sql = """
            UPDATE `vacation`.`vacations`
            SET `countryID` = %s, `description` = %s, `startDate` = %s, `endDate` = %s, `price` = %s, `vacationPictureFile` = %s
            WHERE (`vacationID` = %s);
            """
        params = (countryID,description,startDate,endDate,price,vacationPictureFile, vacationID)
        result = self.dal.update(sql, params)

        if result is not None:

            # Construct SQL query to fetch the newly updated vacation
            sql_update_vacation = "SELECT * FROM vacation.vacations WHERE vacationID = %s"
            new_vacation = self.dal.get_table(sql_update_vacation, (vacationID,))

            return f"Number of rows affected: {result} \nUpdated Vacation: {new_vacation}"
        else:
            return "No rows updated"

    #delete an existing vacation 👍🤩
    def delete_existing_vacation(self, vacationID):
        sql= """
            DELETE FROM `vacation`.`vacations`
            WHERE (`vacationID` = %s);
        """
        params = (vacationID,)
        result = self.dal.delete(sql, params)

        if result is not None:
            return f"Number of rows affected: {result}, vacationID {vacationID} is deleted."
        else:
            return "No rows updated"
    
    def close(self):
        self.dal.close()